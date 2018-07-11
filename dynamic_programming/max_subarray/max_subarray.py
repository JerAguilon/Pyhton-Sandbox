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

    return best_right, best_left, best_total
