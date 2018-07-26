# Given an array, find the largest j - i such that arr[j] > arr[i]

def solution(arr):
    if len(arr) == 0: return -1


    # create start_points, which stores all the indices of elements in which all items to the left are greater
    start_points = [0]
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            start_points.append(i)

    # create a current candidate, which is the right most start point
    curr_candidate = len(start_points) - 1
    curr_left = start_points[curr_candidate]
    curr_right = len(arr) - 1

    best = -1
    while curr_right > 0 and curr_candidate > -1:
        if arr[curr_right] > arr[curr_left]:
            best = max(best, curr_right - curr_left)

            # if we fulfill the condition, then try to make the width wider by going
            # to the next candidate
            curr_candidate -= 1
            curr_left = start_points[curr_candidate]
        else:
            # otherwise, decrease the width to see if we can find a local
            # maximum
            curr_right -= 1
            if curr_right < curr_left:
                curr_candidate -= 1
                curr_left = start_points[curr_candidate]

    return best


    # For reference: The GeeksForGeeks solution, which I find less intuitive
    # left = [0 for _ in range(len(arr))]
    # right = [0 for _ in range(len(arr))]

    # max_right = arr[len(arr) - 1]
    # for i in range(len(arr) - 1, -1, -1):
    #     max_right = max(max_right, arr[i])
    #     right[i] = max_right

    # min_left = arr[0]
    # for i in range(len(arr)):
    #     min_left = min(min_left, arr[i])
    #     left[i] = min_left

    # i = j = 0
    # best = -1

    # while i < len(arr) and j < len(arr):
    #     if left[i] < right[j]:
    #         best = max(best, j - i)
    #         j += 1
    #     else:
    #         i += 1
    # return best

def test():
    assert solution([1,2,3]) == 2
    assert solution([34, 8, 10, 3, 2, 80, 30, 33, 1]) == 6
    assert solution([6, 5,4,3,2,1]) == -1

test()
