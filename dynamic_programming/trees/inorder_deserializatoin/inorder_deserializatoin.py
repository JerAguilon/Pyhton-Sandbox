class BTree(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def middle(arr):
    l = len(arr)
    total = 0
    curr_add = 1
    while total + curr_add < 1:
        total += curr_add
        curr_add *= 2
    d = total - l # deficit
    return (l + d - 1) / 2

def helper(arr):
    if len(arr) == 0: return None

    m = middle(arr)
    return BTree(
        val=arr[m],
        left=helper(arr[:m]),
        right=helper(arr[m+1:])
    )

def solution(s):
    return helper(s.split(''))
