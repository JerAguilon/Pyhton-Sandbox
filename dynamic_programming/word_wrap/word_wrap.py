def build_line_costs(lengths, k):
    extras = [ [0] * (len(lengths))
               for _ in range(len(lengths))]
    for i in range(0, len(lengths)):
        extras[i][i] = k - lengths[i]
        for j in range(i + 1, len(lengths)):
            extras[i][j]= extras[i][j - 1] - lengths[j] - 1


    result = []
    for row in range(len(extras)):
        new_row = [0] * len(extras)
        for col in range(len(extras)):
            if extras[row][col] < 0:
                new_row[col] = float('inf')
            elif col == len(extras) - 1 and extras[row][col] >= 0: # line final
                new_row[col] = 0
            else:
                new_row[col] = extras[row][col]**2
        result.append(new_row)

    return result

def solution(arr, k):
    line_costs = build_line_costs([len(i) for i in arr], k)

    global_costs = [0] * len(arr) # optimized cost to arrange words from 0 to i
    backtrace = []

    for j in range(len(arr)):
        global_costs[j] = float('inf')
        best_i = best_j = -1

        for i in range(0, j + 1):
            if i == 0:
                global_costs[j] = line_costs[i][j]
                best_i = i
                best_j = j
            elif global_costs[i - 1] != float('inf') and global_costs[i - 1] + line_costs[i][j] < global_costs[j]:
                global_costs[j] = global_costs[i - 1] + line_costs[i][j]
                best_i = i
                best_j = j
        backtrace.append([best_i, best_j])

    result = ""
    curr = len(backtrace) - 1
    while True:
        interval = backtrace[curr]
        left = interval[0]
        right = interval[1]

        result = ' '.join(arr[left:right+1]) + '\n' + result
        curr = left - 1
        if curr == -1:
            break
    return result

print(solution(['the', 'cat', 'is', 'back'], 6))
print(solution(['the', 'cat', 'is', 'back'], 7))
