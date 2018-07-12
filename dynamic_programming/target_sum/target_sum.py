# Given an array of integers `arr` and a target number `n`,
# return whether you can reach the target number by adding
# or subtracting the values in the array.
# [1, 2, 1, 5], 3 --> True (1 - 2 - 1 + 5 = 3)
# [1, 2, 1, 4], 3 --> False
# [], 0 --> True
# [1], 0 --> False

# This is actually a simple iteration of the knapsack problem. You have a collection
# of weights that can be positive or negative, and you are looking to fill up
# a knapsack perfectly with some subset of the weights. It's a known NP-complete
# problem. An exponential solution would simply be to try every combination of +/-
# for each item in the list recursively, O(2^n).

# But there's a pseudopolynomial solution to the knapsack problem using DP.
#
# Note that if you subtract all the elements, they would equal some negative number
# -k. If you add them, they would equal some positive number -k. These are some helpful
# upper and lower bounds.
#
# Using this observation, we can create a memoized cache `m` that stores a pair of (`i`, `n`).
# Runtime: O( len(arr) n)


def helper(arr, n, i, m):
    if m.get( (n, i) ):
        return m.get( (n, i) )
    if i == len(arr): return n == 0

    result = helper(arr, n - arr[i], i + 1, m) or helper(arr, n + arr[i], i + 1, m)
    m[(n, i)] = result
    return result

def solution(arr, n):
    return helper(arr, n, 0, {})

def test():
    assert solution([1, 2, 1, 5], 3)
    assert not solution([1, 2, 1, 4], 3)
    assert solution([], 0)
    assert not solution([1], 0)

test()
