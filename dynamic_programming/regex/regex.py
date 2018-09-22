def tokenize(pattern):
    i = 0
    output = []
    while i < len(pattern):
        new_token = pattern[i]
        i += 1
        if i < len(pattern) and pattern[i] == '*':
            new_token += '*'
            i += 1
        output.append(new_token)
    return output

def _matches(tokens, string, i, j, cache):
    if (i, j) in cache:
        return cache[(i, j)]

    if i == len(tokens) and j == len(string):
        return True
    if i == len(tokens):
        cache[(i, j)] = False
        return False

    curr_token = tokens[i]
    if j == len(string):
        result = False if curr_token[-1] != '*' else True
        cache[(i, j)] = result
        return result

    curr_char = string[j]

    if curr_token[-1] == '*':
        if curr_char != curr_token[0]:
            result = _matches(tokens, string, i + 1, j,  cache)
        else:
            result = _matches(tokens, string, i + 1, j, cache) or _matches(tokens, string, i, j + 1, cache)
    else:
        if curr_char != curr_token[0]:
            result = False
        else:
            result = _matches(tokens, string, i + 1, j + 1, cache)

    cache[(i, j)] = result
    return result

def matches(pattern, string):
    tokens = tokenize(pattern)
    cache = {}
    result = _matches(tokens, string, 0, 0, cache)
    print("Memoized Cache: " + str(cache))
    return result


def test():
    assert matches("a*", "aaa")
    assert matches("a*", "")
    assert matches("ca*b", "caaaaab")
    assert matches("ca*b", "cb")


test()
print("All tests passed :)")
