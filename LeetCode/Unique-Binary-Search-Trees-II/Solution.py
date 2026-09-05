1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7# Definition for a binary tree node.
8# class TreeNode:
9#     def __init__(self, val=0, left=None, right=None):
10#         self.val = val
11#         self.left = left
12#         self.right = right
13
14class Solution:
15    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
16        if n == 0:
17            return []
18        
19        memo = {}
20
21        def build_trees(start: int, end: int) -> list[Optional[TreeNode]]:
22            if start > end:
23                return [None]
24            
25            if (start, end) in memo:
26                return memo[(start, end)]
27            
28            trees = []
29            # Pick every value in [start, end] as the root
30            for i in range(start, end + 1):
31                left_trees = build_trees(start, i - 1)
32                right_trees = build_trees(i + 1, end)
33                
34                # Combine left and right subtrees with root i
35                for left in left_trees:
36                    for right in right_trees:
37                        root = TreeNode(i)
38                        root.left = left
39                        root.right = right
40                        trees.append(root)
41                        
42            memo[(start, end)] = trees
43            return trees
44
45        return build_trees(1, n)