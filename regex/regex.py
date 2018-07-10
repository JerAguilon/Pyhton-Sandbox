# here we'll be doing a bottom-up approach for a change
# For this regex, let + match any single character OR the empty character
#                 let * match any arbitrary sequence of characters, including the empty sequence

def matches(curr_p, curr_i):
    if (curr_p == curr_i or curr_p == '+'):
        return True
    return False

def match(input, pattern):
    ilen = len(input) + 1
    plen = len(pattern) + 1

    # Creates an array of height pattern, width input
    result = [ [False] * ilen for _ in range(plen) ]

    result[0][0] = True

    for i in range(1, ilen):
        result[0][i] = False

    is_star = True
    for i in range(1, plen):
        if (pattern[i - 1] == '+'):
            result[i][0] = result[i - 1][0]
        else:
            is_star = (pattern[i - 1] == '*' and is_star)
            result[i][0] = is_star

    for i_pattern in range(1, plen):
        curr_pattern = pattern[i_pattern - 1]
        for i_input in range(1, ilen):
            curr_input = input[i_input - 1]
            if (curr_pattern == '*'):
                result[i_pattern][i_input] = result[i_pattern - 1][i_input - 1] or \
                                             result[i_pattern - 1][i_input] or \
                                             result[i_pattern][i_input - 1]
            elif (curr_pattern == '+'):
                result[i_pattern][i_input] = result[i_pattern - 1][i_input - 1] or \
                                             result[i_pattern - 1][i_input]
            elif matches(curr_pattern, curr_input):
                result[i_pattern][i_input] = result[i_pattern - 1][i_input - 1]
            else:
                result[i_pattern][i_input] = False
    return result[plen - 1][ilen - 1]

def test():
    text = 'baaabab'
    assert match(text, 'ba*a++')
    assert match(text, 'ba*a+')
    assert not match(text, 'a*ab')
    assert match('', '+')
    assert match('', '*')
    assert match('12342134sjdafoiJFI', '+*+I')

    print("Passed :)")

test()
