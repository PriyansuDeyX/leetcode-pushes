1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root) -> bool:
9        def isMirror(t1, t2):
10            if not t1 and not t2: return True
11            if not t1 or not t2: return False
12            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
13        
14        return isMirror(root, root)