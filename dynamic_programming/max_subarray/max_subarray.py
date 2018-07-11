# Given a 2D array, return the rectangle with the maximum sum of all elements.
# https://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/

def kadane(arr):
    best_right = best_left = best_total = 0

    left = right = curr_total = 0
    while right < len(arr):
        curr_total += arr[right]

        if curr_total < 0:
            left = right + 1
            curr_total = 0
        elif curr_total > best_total:
            best_right, best_left, best_total = right, left, curr_total
        right += 1

    return best_left, best_right, best_total

def solution(arr): # 2-D Array
    best_top = best_left = best_bottom = best_right = best_total = 0

    if len(arr) < 0 or len(arr[0]) < 0:
        return (best_left, best_top), (best_right, best_bottom), best_total

    for left in range(len(arr[0])):
        curr = [0] * len(arr)

        for right in range(left, len(arr[0])):
            for i in range(len(arr)):
                curr[i] += arr[i][right]

            if left == 1 and right == 3:
                print(curr)
            top, bottom, curr_total = kadane(curr)
            if (curr_total > best_total):
                best_top, best_left, best_bottom, best_right, best_total = \
                        (top, left, bottom, right, curr_total)

    return (best_left, best_top), (best_right, best_bottom), best_total

def test():
    test_arr = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]

    print(solution(test_arr))

test()
