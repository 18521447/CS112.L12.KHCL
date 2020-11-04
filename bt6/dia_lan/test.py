import os
from typing import Iterable, Optional, Union, Tuple

import numpy as np
from numpy.random import randint

np.random.seed(0)


def shuffle(matrix: np.ndarray):
    """
        Shuffle rows and columns of the bit matrix
    """
    np.random.shuffle(matrix)
    np.random.shuffle(matrix.transpose())


def random_bool(size: Union[int, Iterable, Tuple[int], None] = None) -> Union[bool, int, np.ndarray]:
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

        self.__one_combination: bool = random_bool()
        self.__use_col_one: bool = True if self.is_no and self.k >= self.__max_number_of_bits else random_bool()

        current_config = \
            "Current config:\n" + \
            "   - n={}\n".format(self.n) + \
            "   - k={}\n".format(self.k) + \
            "   - output_is_yes={}\n".format(self.__is_yes) + \
            "   - one_combination={}\n".format(self.__one_combination) + \
            "   - use_col_one={}\n".format(self.__use_col_one) + \
            "   - max_number_of_bits={}\n".format(self.max_number_of_bits)

        # How to choose randomly a suitable size (__real_k) for top_right matrix
        #     no  -> kdb >= maxbit -> use_col_one
        #         -> kdb  < maxbit -> use_col_one
        #                          ->   one_C            -> ktt(kdb..min(n, maxbit)]
        #                          ->  more_C            -> ktt(kdb..min(n - 1, maxbit)]
        #
        #     yes -> kdb > maxbit  -> one_C             -> ktt[1..maxbit]
        #                          -> more_C            -> ktt[1..maxbit]
        #         -> kdb <= maxbit -> one_C             -> ktt[1..kdb]
        #                          -> more_C -> kdb = n -> ktt[1..kdb)
        #                                    -> kdb < n -> ktt[1..kdb]
        # Check error
        # if k == 1 and n == 1 and not one_combination:
        #     raise ValueError("n is not large enough to create more combinations\n"
        #                      "Current config:\n"
        #                      "  - n={}\n"
        #                      "  - k={}\n"
        #                      "  - output_is_yes={}\n"
        #                      "  - one_combination={}".format(n, k, output_is_yes, one_combination))

        __N_NOT_LARGE_ENOUGH = "n is not large enough to create more combinations\n"

        if self.is_yes and self.__use_col_one:
            raise ValueError("Test output is YES so all the columns must have at least one zero\n" +
                             current_config)

        if not self.is_yes and k >= max_number_of_bits:
            if not self.__use_col_one:
                raise ValueError("Output is NO and k >= max_number_of_bits so all columns mustn't have any 0\n" +
                                 current_config)

        # Choose randomly a suitable size for top_right matrix
        if self.is_no and not self.__use_col_one:
            n_bound = self.n if self.__one_combination else self.n - 1
            try:
                self.__real_k = randint(self.k + 1, min(n_bound, self.max_number_of_bits) + 1)
            except ValueError:
                raise ValueError(__N_NOT_LARGE_ENOUGH + current_config)
        elif self.is_yes:
            if self.k > self.max_number_of_bits:
                self.__real_k = randint(1, self.max_number_of_bits + 1)
            else:
                if self.__one_combination or self.k < self.n:
                    self.__real_k = randint(1, self.k + 1)
                else:
                    try:
                        self.__real_k = randint(1, self.k)
                    except ValueError:
                        raise ValueError(__N_NOT_LARGE_ENOUGH + current_config)

        self.__generate_new_bit_matrix()

    @property
    def n(self) -> int:
        return self.__n

    @property
    def k(self) -> int:
        return self.__k

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
        for row in self.__bit_matrix:
            cache.append(str(int(''.join(map(str, row)), 2)))
            cache.append(' ')
        cache.pop()
        return ''.join(cache)

    @property
    def output(self) -> str:
        return "YES\n" if self.__is_yes else "NO\n"

    def __generate_new_bit_matrix(self):
        """
            Each row of the bit matrix corresponds to a decimal number
        """
        if self.__use_col_one:
            row_count: int = self.n
            col_count: int = self.max_number_of_bits
            self.__bit_matrix = random_bool((row_count, col_count))
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
        matrix = random_bool((row_count, col_count))

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
        row_count = self.n - self.__real_k
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
        row_count = self.n - self.__real_k
        col_count: int = self.max_number_of_bits - self.__real_k
        return random_bool((row_count, col_count))

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
    t = True
    f = False
    # for n_ in np.arange(11, 13):
    #     for k_ in np.arange(1, n_ + 1):
    #         if n_ == 1 and k_ == 1:
    #             continue
    #         DiaLanTestCreator(n_,
    #                           k_,
    #                           output_is_yes=t,
    #                           one_combination=t,
    #                           use_col_one=f).write_to_disk(str(id_), save_path)
    #         id_ += 1
    #         # DiaLanTestCreator(n_,
    #         #                   k_,
    #         #                   output_is_yes=t,
    #         #                   one_combination=f,
    #         #                   use_col_one=t).write_to_disk(str(id_), save_path)
    #         # id_ += 1
    #
    #         DiaLanTestCreator(n_,
    #                           k_,
    #                           output_is_yes=t,
    #                           one_combination=f,
    #                           use_col_one=f).write_to_disk(str(id_), save_path)
    #         id_ += 1
    #         DiaLanTestCreator(n_,
    #                           k_,
    #                           output_is_yes=f,
    #                           one_combination=t,
    #                           use_col_one=t).write_to_disk(str(id_), save_path)
    #         id_ += 1
    #         if not (n_ == k_ or k_ >= 12):
    #             DiaLanTestCreator(n_,
    #                               k_,
    #                               output_is_yes=f,
    #                               one_combination=t,
    #                               use_col_one=f).write_to_disk(str(id_), save_path)
    #             id_ += 1
    #         DiaLanTestCreator(n_,
    #                           k_,
    #                           output_is_yes=f,
    #                           one_combination=f,
    #                           use_col_one=t).write_to_disk(str(id_), save_path)
    #         id_ += 1
    #         if not (k_ + 1 >= n_ - 1):
    #
    #             DiaLanTestCreator(n_,
    #                               k_,
    #                               output_is_yes=f,
    #                               one_combination=f,
    #                               use_col_one=f).write_to_disk(str(id_), save_path)
    #             id_ += 1
    #
    usecolone_count = 0
    one_com_count = 0
    more_com_count = 0
    for n_ in np.arange(1, 13):
        for k_ in np.arange(1, n_ + 1):
            test = DiaLanTestCreator(n_, k_, is_yes=f)
            test.write_to_disk(str(id_), save_path)
            if test.use_col_one:
                usecolone_count += 1
            elif test.one_combination:
                one_com_count += 1
            else:
                more_com_count += 1
            id_ += 1
    print(usecolone_count)
    print(one_com_count)
    print(more_com_count)
