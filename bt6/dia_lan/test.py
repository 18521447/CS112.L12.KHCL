import os
from typing import Iterable, Union, Optional

import numpy as np
from numpy.random import randint

np.random.seed(0)


def shuffle(matrix: np.ndarray):
    """
        Shuffle rows and columns of the bit matrix
    """
    np.random.shuffle(matrix)
    np.random.shuffle(matrix.transpose())


def random_bits(size: Union[int, Iterable, None] = None) -> Union[int, np.ndarray]:
    return randint(2, size=size, dtype=np.uint8)


class DiaLanTestCreator:
    """
        Class to create test for Dia Lan exercise
    """

    def __init__(self, n, k, is_yes, max_number_of_bits=12):
        """
        :param int n: input length of array
        :param int k: input number of elements of one combination
        :param bool is_yes: Control the output
        :param int max_number_of_bits: Maximum number of bits for each element of the array
        """

        if n < k:
            raise ValueError("n < k ({} < {})".format(n, k))

        if max_number_of_bits < 1:
            raise ValueError("max_number_of_bits < 1 ({} < 1)".format(max_number_of_bits))

        self.__n: int = n
        self.__k: int = k
        self.__max_number_of_bits: int = max_number_of_bits
        self.__is_yes: bool = is_yes

        self.__one_combination: bool = True
        if self.k != 1 and self.n != 1:
            self.__one_combination = bool(random_bits())

        self.__use_col_one = False
        if self.is_no:
            self.__use_col_one = True if self.k >= self.max_number_of_bits else bool(random_bits())

        self.current_config = \
            "Current config:\n" + \
            "   - n={}\n".format(self.n) + \
            "   - k={}\n".format(self.k) + \
            "   - output_is_yes={}\n".format(self.__is_yes) + \
            "   - one_combination={}\n".format(self.__one_combination) + \
            "   - use_col_one={}\n".format(self.__use_col_one) + \
            "   - max_number_of_bits={}\n".format(self.max_number_of_bits)

        if self.is_yes and self.__use_col_one:
            raise ValueError("Test output is YES so all the columns must have at least one zero\n" +
                             self.current_config)

        if self.is_no and k >= max_number_of_bits and not self.__use_col_one:
            raise ValueError("Output is NO and k >= max_number_of_bits so all columns mustn't have any 0\n" +
                             self.current_config)

        # How to choose randomly a suitable size (__real_k) for top_right matrix
        #     no  -> kdb >= maxbit -> use_col_one
        #         -> kdb  < maxbit -> use_col_one
        #                          ->   one_C            -> ktt(kdb..maxbit]
        #                          ->  more_C            -> ktt(kdb..maxbit]
        #
        #     yes -> kdb > maxbit  -> one_C             -> ktt[1..maxbit]
        #                          -> more_C            -> ktt[1..maxbit]
        #         -> kdb <= maxbit -> one_C             -> ktt[1..kdb]
        #                          -> more_C -> kdb = n -> ktt[1..kdb)
        #                                    -> kdb < n -> ktt[1..kdb]

        # Choose randomly a suitable size (self.__real_k) for top_right matrix
        real_k_min = 1
        real_k_max = self.max_number_of_bits + 1

        if self.is_no and not self.use_col_one:
            real_k_min = min(self.k, self.max_number_of_bits) + 1
        elif self.is_yes:
            if self.k <= self.max_number_of_bits:
                real_k_max = min(self.k, self.max_number_of_bits) + 1
            if not self.one_combination and self.k == n:
                real_k_max -= 1

        self.__real_k: int = randint(real_k_min, real_k_max)

        self.__generate_new_bit_matrix()

    @property
    def n(self) -> int:
        return self.__n

    @property
    def k(self) -> int:
        return self.__k

    @property
    def real_k(self) -> Optional[int]:
        return None if self.use_col_one else self.__real_k

    @property
    def max_number_of_bits(self) -> int:
        return self.__max_number_of_bits

    @property
    def is_yes(self) -> bool:
        return self.__is_yes

    @property
    def is_no(self) -> bool:
        return not self.__is_yes

    @property
    def one_combination(self) -> bool:
        return self.__one_combination

    @property
    def use_col_one(self) -> bool:
        return self.__use_col_one

    @property
    def input(self) -> str:
        cache = [str(self.n), ' ', str(self.k), '\n']
        for r in range(self.n):
            bits_str = ''.join(map(str, self.__bit_matrix[r]))
            decimal = int(bits_str, 2)
            cache.append(str(decimal))
            cache.append(' ')
        cache.pop()
        return ''.join(cache)

    @property
    def output(self) -> str:
        return "YES\n" if self.__is_yes else "NO\n"

    @property
    def bit_matrix(self) -> np.ndarray:
        return self.__bit_matrix

    def __generate_new_bit_matrix(self):
        """
            Each row of the bit matrix corresponds to a decimal number
        """
        if self.__use_col_one:
            row_count = self.n
            col_count = self.max_number_of_bits
            self.__bit_matrix = random_bits((row_count, col_count))
            total_cols_one = randint(1, col_count + 1)
            cols_one_mask = randint(0, col_count, size=total_cols_one)
            self.__bit_matrix[:, cols_one_mask] = 1
            return

        top_right = self.__generate_top_right()
        top_left = self.__generate_top_left()
        bottom_right = self.__generate_bottom_right()
        bottom_left = self.__generate_bottom_left()
        self.__bit_matrix = np.block([[top_left, top_right],
                                      [bottom_left, bottom_right]])
        shuffle(self.__bit_matrix)

    def __generate_top_right(self) -> np.ndarray:
        """
            Return a new __real_k x __real_k square matrix with zeros on the main diagonal and ones elsewhere
        """
        matrix = 1 - np.identity(self.__real_k, np.uint8)
        shuffle(matrix)
        return matrix

    def __generate_top_left(self) -> np.ndarray:
        """
            Return a random k x (max_number_of_bits - k) matrix
        """
        row_count = self.__real_k
        col_count = self.max_number_of_bits - self.__real_k
        matrix = random_bits((row_count, col_count))

        if col_count == 0:
            return matrix

        cols_all_ones = (matrix == 1).all(0)
        total_col_all_ones = np.sum(cols_all_ones)
        random_rows = randint(self.__real_k, size=total_col_all_ones)
        matrix[random_rows, cols_all_ones] = 0

        return matrix

    def __generate_bottom_right(self) -> np.ndarray:
        """
            Return a random (n - k) x k matrix representing padding bits below the core matrix.
        """
        row_count = max(self.n - self.__real_k, 0)
        col_count = self.__real_k
        matrix = np.ones((row_count, col_count), np.uint8)

        if row_count == 0 or self.__one_combination:
            return matrix

        row_range = np.arange(row_count)
        random_cols = randint(col_count, size=row_count)
        matrix[row_range, random_cols] = 0

        return matrix

    def __generate_bottom_left(self) -> np.ndarray:
        """
            Return a random (n - k) x (max_number_of_bits - k) matrix
        """
        row_count = max(self.n - self.__real_k, 0)
        col_count: int = self.max_number_of_bits - self.__real_k
        return random_bits((row_count, col_count))

    def write_to_disk(self, filename: str, location: str = '.'):
        input_file = os.path.join(location, 'inp', filename)
        output_file = os.path.join(location, 'out', filename)
        with open(input_file, 'w') as inp:
            inp.write(self.input)
        with open(output_file, 'w') as out:
            out.write(self.output)


if __name__ == '__main__':
    save_path = "C:\\Users\\Thinh\\code\\python\\CS112.L12.KHCL\\bt6\\dia_lan\\tests_draft"

    id_ = 1

    for n_ in np.arange(1, 20):
        for k_ in np.arange(1, n_ + 1):
            DiaLanTestCreator(n_, k_, True).write_to_disk(str(id_), save_path)
            id_ += 1
            DiaLanTestCreator(n_, k_, False).write_to_disk(str(id_), save_path)
            id_ += 1

    # a = DiaLanTestCreator(1, 1, False)
    # print(a.input)
    # print(a.output)
    # print()
    # print(a.current_config)
    # id_ += 1
    # print(id_)
