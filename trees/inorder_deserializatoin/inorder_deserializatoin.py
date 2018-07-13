# Consider this binary tree:
#      a
#    b   c
#  d   e
# Clearly, an inorder serialization would be "dbeac"
#
# For this problem, we are given an arbitary string. Construct a binary
# tree out of it, except with the following constraint: the binary tree
# must be complete. i.e. Any extra nodes should be from left to right.
#
# Complete BTree definition:
# http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/FullvsComplete.html
#
# For example, for "dbeac", the following is invalid:
#
#       a
#     e   c
#   b
# d

class BTree(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# deficit: 2
# l + d + 1 = len(arr)
#

def middle(arr):
    l = len(arr) #d b e a c
    total = 0
    curr_add = 1
    while total + curr_add <= l:
        total += curr_add
        curr_add *= 2
    d = l - total # deficit
    return int((l + d - 1) / 2)

def helper(arr):
    if len(arr) == 0: return None

    m = middle(arr)
    return BTree(
        val=arr[m],
        left=helper(arr[:m]),
        right=helper(arr[m+1:])
    )

def solution(s):
    return helper(list(s))

'''
Test code
'''
def test_solution(s):
    root = solution(s)

    def assert_string_match(s, root):
        def get_string(root):
            if root is None: return ''
            return get_string(root.left) + root.val + get_string(root.right)
        assert s == get_string(root)

    def assert_is_complete(s, i, root):
        if root is None: return

        assert i < len(s)

        assert_is_complete(s, 2*i+1, root.left)
        assert_is_complete(s, 2*i+2, root.right)

    assert_string_match(s, root)
    assert_is_complete(s, 0, root)


def test():
    test_solution('dbeac')
    test_solution('')
    test_solution('a')
    test_solution('abcdefghijklmnop')
    test_solution('abcdefghijklmnopq')

test()