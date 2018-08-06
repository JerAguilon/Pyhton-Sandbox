def solution(str):
    if len(str) == 0: return 0
    if any([letter not in {'b','a','r','k'} for letter in str]):
        return -1

    borking_doggos = {
        'b': 0,
        'ba': 0,
        'bar': 0,
    }

    next = {
        'b': 'b',
        'a': 'ba',
        'r': 'bar',
    }
    prev = {
        'a': 'b',
        'r': 'ba',
        'k': 'bar',
    }

    result = 0
    curr_borking_doggos = 0

    for i in str:
        if i in next:
            borking_doggos[next[i]] += 1
        if i in prev:
            borking_doggos[prev[i]] -= 1
            if borking_doggos[prev[i]] < 0:
                return -1
        if i == 'b':
            curr_borking_doggos += 1
            result = max(result, curr_borking_doggos)
        if i == 'k':
            curr_borking_doggos -= 1

    return result if result > 0 else -1

print(solution('bark'))
print(solution('bbaarrkk'))
print(solution('bk'))
print(solution('brak'))
print(solution('bak'))
