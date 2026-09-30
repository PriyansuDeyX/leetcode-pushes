1class Solution:
2    def maxDepthAfterSplit(self, seq: str) -> list[int]:
3        ans = []
4        depth = 0
5        for char in seq:
6            if char == '(':
7                depth += 1
8                ans.append((depth - 1) % 2)
9            else:
10                ans.append((depth - 1) % 2)
11                depth -= 1
12        return ans