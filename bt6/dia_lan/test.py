import numpy as np


def shuffle(matrix: np.ndarray):
    """
        Shuffle rows and columns of the bit matrix
    """
    np.random.shuffle(matrix)
    np.random.shuffle(matrix.transpose())


class DiaLanTest:
    """
        Class to create test for Dia Lan exercises
    """

    def __init__(self,
                 n,
                 k,
                 output_is_yes,
                 one_combination,
                 use_col_one=False,
                 max_number_of_bits=12):
        """
        :param int n: number of elements in this test
        :param int k: number of elements in one combination
        :param bool output_is_yes: If True then this test have combination(s) of k numbers that equals 0
        :param bool one_combination: This test have exactly one combination of k numbers equals 0
        :param bool use_col_one: If use_col_one is True then the result matrix has at least one column full of bit 1
        :param int max_number_of_bits: Maximum number of bits for each element in this test
        """
        if n < k:
            raise ValueError("n can't be less than k ({} < {})".format(n, k))
        if max_number_of_bits < 1:
            raise ValueError("max_number_of_bits can't be less than 1")
        if output_is_yes and use_col_one:
            raise ValueError("Test output is YES so use_col_one must be False")
        if not output_is_yes and k >= max_number_of_bits:
            if not use_col_one:
                raise ValueError("Output is NO and k >= max_number_of_bits so use_col_one must be True")

        np.random.seed(23)

        self.__n: int = n
        self.__k: int = k
        self.__real_k = self.k
        self.__max_number_of_bits: int = max_number_of_bits
        self.__is_yes: bool = output_is_yes
        self.__one_combination: bool = one_combination
        self.__use_col_one = use_col_one

        # Pick randomly a suitable size (__real_k) for top_right matrix
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
        if self.is_no and not self.__use_col_one:
            n_bound = self.n - 1 if self.__one_combination else self.n
            self.__real_k = np.random.randint(self.k + 1, min(n_bound, self.max_number_of_bits) + 1)
        elif self.is_yes:
            if self.k > self.max_number_of_bits:
                self.__real_k = np.random.randint(1, self.max_number_of_bits + 1)
            else:
                if self.__one_combination or self.k < self.n:
                    self.__real_k = np.random.randint(1, self.k + 1)
                else:
                    self.__real_k = np.random.randint(1, self.k)

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
    def input(self) -> str:
        cache = [self.n, ' ', self.k, '\n']
        for row in self.__bit_matrix:
            cache.append(str(int(''.join(map(str, row)), 2)))
            cache.append(' ')
        cache.pop()
        return ''.join(cache)

    @property
    def output(self) -> str:
        return "YES\n" if self.__is_yes else "NO\n"

    @property
    def is_yes(self) -> bool:
        return self.__is_yes

    @property
    def is_no(self) -> bool:
        return not self.__is_yes

    def __generate_new_bit_matrix(self):
        """
            Each row of the bit matrix corresponds to a decimal number
        """
        if self.__use_col_one:
            row_count: int = self.n
            col_count: int = self.max_number_of_bits
            self.__bit_matrix = np.random.randint(2, size=(row_count, col_count), dtype=np.uint8)
            total_cols_one = np.random.randint(1, col_count + 1)
            cols_one_mask = np.random.randint(0, col_count, size=total_cols_one)
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
        matrix = np.random.randint(2, size=(row_count, col_count), dtype=np.uint8)

        if col_count == 0:
            return matrix

        col_all_ones = (matrix == 1).all(0)
        total_col_all_ones = np.sum(col_all_ones)
        matrix[np.random.randint(2, size=total_col_all_ones), col_all_ones] = 0

        return matrix

    def __generate_bottom_right(self) -> np.ndarray:
        """
            Return a random (n - k) x k matrix representing padding bits below the core matrix.
        """
        row_count: int = self.n - self.__real_k
        col_count: int = self.__real_k
        matrix = np.ones((row_count, col_count), np.uint8)

        if row_count == 0 or self.__one_combination:
            return matrix

        row_range = np.arange(row_count)
        random_cols = np.random.randint(col_count, size=row_count)
        matrix[row_range, random_cols] = 0

        return matrix

    def __generate_bottom_left(self) -> np.ndarray:
        """
            Return a random (n - k) x (max_number_of_bits - k) matrix
        """
        row_count = self.n - self.__real_k
        col_count = self.max_number_of_bits - self.__real_k
        return np.random.randint(2, size=(row_count, col_count), dtype=np.uint8)
