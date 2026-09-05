1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
10        if n == 0:
11            return []
12        
13        memo = {}
14
15        def build_trees(start: int, end: int) -> list[Optional[TreeNode]]:
16            if start > end:
17                return [None]
18            
19            if (start, end) in memo:
20                return memo[(start, end)]
21            
22            trees = []
23            # Pick every value in [start, end] as the root
24            for i in range(start, end + 1):
25                left_trees = build_trees(start, i - 1)
26                right_trees = build_trees(i + 1, end)
27                
28                # Combine left and right subtrees with root i
29                for left in left_trees:
30                    for right in right_trees:
31                        root = TreeNode(i)
32                        root.left = left
33                        root.right = right
34                        trees.append(root)
35                        
36            memo[(start, end)] = trees
37            return trees
38
39        return build_trees(1, n)