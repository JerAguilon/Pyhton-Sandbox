def helper(arr, n, i, m):
    if (n == 0): return i == len(arr)
    result = helper(arr, n - arr[i], i + 1, m) or helper(arr, n + arr[i], i + 1, m)
    m[(n, i)] = result
    return result

def solution(arr, n):
    return helper(arr, n, 0, {})

def test():
    assert solution([1, 2, 1, 5], 3)
