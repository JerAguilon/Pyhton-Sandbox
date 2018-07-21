def longestPalindrome(s):
    result_l = result_r = 0
    n = len(s)
    table = [ [False] * len(s) for _ in range(len(s)) ] # len(s) x len(s) array
    for i in range(0, len(table)):
        table[i][i] = True
    for i in range(0, len(table) - 1):
        if s[i] == s[i + 1]:
            table[i][i+1] = True
            result_l = i
            result_r = i+1

    for size in range(3, len(table) + 1):
        for left in range(0, len(table) - size + 1):
            right = left + size - 1
            if table[left + 1][right- 1] and s[left] == s[right]:
                table[left][right] = True
                if right - left > result_r - result_l:
                    result_l = left
                    result_r = right
    return s[result_l:result_r + 1]
  
assert("bdcddcdboiwjefoiwjeaiojaaa") == "dcddcd"
