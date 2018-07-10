# here we'll be doing a bottom-up approach for a change
# For this regex, let + match any single empty character
#                 let * match any arbitrary sequence of characters, including the empty sequence

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
        is_star = pattern[i - 1] == '*';
        result[i][0] = is_star

    for i_pattern in range(1, plen):
        curr_pattern = pattern[i_pattern - 1]
        for i_input in range(1, ilen):
            curr_input = input[i_input - 1]
    return result[plen - 1][ilen - 1]
