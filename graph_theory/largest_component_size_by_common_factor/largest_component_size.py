# Leetcode #952

import math

class Solution(object):
    def __has_valid_common_factor(self, a, b):
        lower = min(a, b)
        higher = max(a, b)

        if higher % lower == 0:
            return True
        for i in range(2, int(math.sqrt(lower))):
            if higher % i == 0 and lower % i == 0:
                return True
        return False

    def __get_size(self, index, A):
        A[index] = -1
        total = 1
        for next_index, next_value in enumerate(A):
            if next_value != -1 and self.__has_valid_common_factor(A[index], next_value):
                total += self.__get_size(next_index, A)
        return total

    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largest = 0
        for index, value in enumerate(A):
            if value != -1:
                largest = max(largest, self.__get_size(index, A))
        return largest

def assert_solution(A, expected):
    result = Solution().largestComponentSize([4, 6, 15, 35])
    assert result == expected, "RESULT: {}, EXPECTED: {}".format(result, expected)

def test():
    assert_solution([4, 6, 15, 35], 4)

test()
