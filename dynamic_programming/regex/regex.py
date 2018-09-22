# Problem: Create method matches(pattern, string) that returns whether a pattern matches a string.
# * after a character means that the previous character can match unlimited times, including no times.
# Note: * is called a 'wildcard match'
#
# Test cases:
#  a* matches aaaaa, "" (empty string), a, etc.
#  ca*b matches caaaaab, cab, cb, etc.


'''
Tokenize the pattern string into an array of tokens. For example,
pattern = "ca*b" --> ['c', 'a*', 'b']
'''
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

'''
Recursively checks if the string matches the pattern using a cache to improve runtime to O(len(pattern) * len(string))

Inputs:
    tokens - the list of tokens in of the pattern
    string - the string we are testing
    i - the index of the token we're processing
    j - the index of the string we're processing

'''
def _matches(tokens, string, i, j, cache):
    '''
    Base Cases:
        1) If (i, j) was already solved before, return that
        2) If i and j are both at the end of tokens/string, then we found a match
        3) If i is at the end of tokens, but there's more strings left, then we don't have a match
        4) If j is at the end of string, then there are two cases. If the current token isn't a '*' token, then
           for sure the strings don't match. Otherwise, we need to increment i and test for that since * matches
           the empty string too
    '''

    if (i, j) in cache:
        return cache[(i, j)]

    if i == len(tokens) and j == len(string):
        return True
    if i == len(tokens):
        cache[(i, j)] = False
        return False

    curr_token = tokens[i]
    if j == len(string):
        if curr_token[-1] == '*':
            result = _matches(tokens, string, i + 1, j, cache)
        else:
            result = False
        cache[(i, j)] = result
        return result

    curr_char = string[j]

    '''
    Recursive cases:
        1) If the current token has a '*', then there are two cases:
              a) curr_char != curr_token --> Increment i and test for that, since the pattern can match the empty
                 string
              b) curr_char == curr_token --> test for (i + 1, j), the empty string AND (i, j + 1), the wildcard match
        2) If the current token is just a character, then simply check that the pattern and string match and
           recur for (i + 1, j + 1)
    '''
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
