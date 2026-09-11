1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: TreeNode | None) -> bool:
9        def validate(node: TreeNode | None, low: int, high: int) -> bool:
10            # An empty tree is a valid BST
11            if not node:
12                return True
13            
14            # The current node's value must be strictly between low and high
15            if not (low < node.val < high):
16                return False
17            
18            # Recursively validate left and right subtrees with updated bounds
19            return (validate(node.left, low, node.val) and 
20                    validate(node.right, node.val, high))
21
22        return validate(root, float('-inf'), float('inf'))