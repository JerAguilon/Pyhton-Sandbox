# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# Given a binary tree, return the zigzag level order traversal of its nodes’ 
# values. (ie, from left to right, then right to left for the next level and alternate between).

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        should_reverse = True
        curr = [A]
        result = []
        
        while len(curr) > 0:
            next = []
            sub_result = []
            for n in curr:
                sub_result.append(n.val)
                if n.right: next.append(n.right)
                if n.left: next.append(n.left)
            curr = next
            if should_reverse: sub_result.reverse()
            result.append(sub_result)
            should_reverse = not should_reverse
            
        return result
