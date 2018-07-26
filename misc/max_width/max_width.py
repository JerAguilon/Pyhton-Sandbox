def solution(arr):
    left = [0 for _ in range(len(arr))]
    right = [0 for _ in range(len(arr))]

    max_right = arr[len(arr) - 1]
    for i in range(len(arr) - 1, -1, -1):
        max_right = max(max_right, arr[i])
        right[i] = max_right

    min_left = arr[0]
    for i in range(len(arr)):
        min_left = min(min_left, arr[i])
        left[i] = min_left

    i = j = 0
    best = -1

    while i < len(arr) and j < len(arr):
        if left[i] < right[j]:
            best = max(best, j - i)
            j += 1
        else:
            i += 1
    return best

def test():
    assert solution([1,2,3]) == 2
    assert solution([34, 8, 10, 3, 2, 80, 30, 33, 1]) == 6
    assert solution([6, 5,4,3,2,1]) == -1

test()
