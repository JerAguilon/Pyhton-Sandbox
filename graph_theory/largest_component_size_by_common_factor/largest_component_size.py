# Leetcode #952

from math import floor
from collections import defaultdict
class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        def find(n):
            if p[n]!=n:
                p[n], _ = find(p[n])
            return p[n], c[p[n]]
        def union(x, y):
            px, cx = find(x)
            py, cy = find(y)
            if px != py:
                c[px] = cx + cy
            p[py] = px
        def factors(dicts, n, idx):
            onlyme = True
            for i in range(2, int(floor(n ** 0.5) + 1)):
                if n %i ==0:
                    for k in [i, n//i]:
                        prime = True
                        for j in range(2, int(floor(k ** 0.5) + 1)):
                            if k%j == 0:
                                prime = False
                                break
                        if prime == True:
                            dicts[k].add(idx)
                            onlyme = False
            if onlyme:
                dicts[n].add(idx)

        # myset = [None for _ in A]
        # for i, n in enumerate(A):
        #     myset[i] = factors(n)
        # sets = set.union(*myset)
        dicts = defaultdict(set)
        for i, n in enumerate(A):
            factors(dicts,n, i)
        p = [i for i in range(len(A))]
        c = [1 for i in range(len(A))]

        for key, val in dicts.items():
            if len(val)>1:
                pre = val.pop()
                while (val):
                    cur = val.pop()
                    union(pre, cur)
                    pre = cur
        return max(c)

def assert_solution(A, expected):
    copy = list(A)
    result = Solution().largestComponentSize(A)
    assert result == expected, "RESULT: {}, EXPECTED: {}".format(result, expected)
    print("PASSED: {} => {}".format(copy, expected))

def test():
    assert_solution([4, 6, 15, 35], 4)
    assert_solution([20, 50, 9, 63], 2)
    assert_solution([2,3,6,7,4,12,21,39], 8)
    assert_solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 11)

test()
