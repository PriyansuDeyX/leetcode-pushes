1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        # Jodi tree khali ba node null hoy, tahole kono path nai
10        if not root:
11            return False
12        
13        # Jodi eta ekta leaf node hoy (tar kono child nei), tahole dekhi baki targetSum-er soman kina
14        if not root.left and not root.right:
15            return targetSum == root.val
16        
17        # Current node-er value bad diye baki sum ta ber korchi
18        remaining_sum = targetSum - root.val
19        
20        # Left ba right je kono ekta sub-tree theke valid path pele true return korbo
21        # dsa copy 3 (debdutta mam er notes)
22
23        return (self.hasPathSum(root.left, remaining_sum) or 
24                self.hasPathSum(root.right, remaining_sum))