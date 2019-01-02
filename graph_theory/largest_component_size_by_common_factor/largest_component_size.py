# Leetcode #952

import math

class Solution(object):
    def __has_valid_common_factor(self, a, b):
        lower = min(a, b)
        higher = max(a, b)

        if higher % lower == 0:
            return True
        for i in range(2, int(math.sqrt(lower) + 1)):
            if lower % i == 0:
                j = lower / i
                if higher % i == 0 or higher % j == 0:
                    return True
        return False

    def __get_size(self, value, A):
        total = 1
        A.remove(value)
        curr_iter = iter(A)
        next_value = next(curr_iter, None)
        while next_value:
            if self.__has_valid_common_factor(value, next_value):
                total += self.__get_size(next_value, A)
                curr_iter = iter(A)
            next_value = next(curr_iter, None)
        print("RETURNING" + str(total))
        return total

    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largest = 0
        A = set(A)
        while len(A) > 0:
            next_value = next(iter(A))
            if next_value == 1:
                A.remove(next_value)
            else:
                largest = max(largest, self.__get_size(next_value, A))
        return largest

def assert_solution(A, expected):
    copy = list(A)
    result = Solution().largestComponentSize(A)
    assert result == expected, "RESULT: {}, EXPECTED: {}".format(result, expected)
    print("PASSED: {} => {}".format(copy, expected))

def test():
    assert_solution([4, 6, 15, 35], 4)
    assert_solution([20, 50, 9, 63], 2)
    assert_solution([2,3,6,7,4,12,21,39], 8)

test()
