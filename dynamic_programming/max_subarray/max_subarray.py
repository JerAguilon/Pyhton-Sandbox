def kadane(arr):
    best_right = best_left = best_total = 0

    left = right = curr_total = 0
    while right < len(arr):
        curr_total += arr[right]

        if curr_total < 0:
            left = right + 1
        elif curr_total > best_total:
            best_right, best_left, best_total = right, left, curr_total
        right += 1

    return best_left, best_right, best_total

def solution(arr): # 2-D Array
    best_top = best_left = best_bottom = best_right = best_total = 0

    if len(arr) < 0 or len(arr[0]) < 0:
        return (best_left, best_top), (best_right, best_bottom), best_total

    for left in len(arr[0]):
        curr = [ [0] * len(arr) ]

        for right in len(left, arr[0]):
            for i in len(arr):
                curr[i] += arr[i][right]
            top, bottom, curr_total = kadane(curr)
            if (curr_total > best_total):
                best_top, best_left, best_bottom, best_right, best_total = \
                        (top, left, bottom, right, curr_total)

    return (best_left, best_top), (best_right, best_bottom), best_total
