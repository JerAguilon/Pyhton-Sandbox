'''
Given a list of stock prices, return the most
amount of money you can make if you can buy
and sell up to two times. Note that you can only do the
following:

buy -> sell -> buy -> sell
buy -> sell
Do nothing

Patterns like buy -> buy-> sell -> sell aren't valid.
'''
def solution(arr):
    n = len(arr)

    memoized = []

    lowest_so_far = arr[0]
    curr_best = 0
    for i in range(n):
        if arr[i] < lowest_so_far:
            lowest_so_far = arr[i]
        curr_best = max(curr_best, arr[i] - lowest_so_far)
        memoized.append( [curr_best, None] )

    greatest_so_far = arr[n - 1]
    curr_best = 0
    for i in range(n - 1, -1, -1):
        if arr[i] > greatest_so_far:
            greatest_so_far = arr[i]
        curr_best = max(curr_best, greatest_so_far - arr[i])
        memoized[i][1] = curr_best

    candidates = [ i[0] + i[1] for i in memoized ]

    return max(candidates)

assert solution([2, 30, 15, 10, 8, 25, 80]) == 100
assert solution([10, 22, 5, 75, 65, 80]) == 87
assert solution([100, 30, 15, 10, 8, 25, 80]) == 72
assert solution([90, 80, 70, 60, 50]) == 0
print("All tests passed :)")
