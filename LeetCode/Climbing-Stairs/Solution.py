1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2: return n
4        a, b = 1, 2
5        for _ in range(3, n + 1):
6            a, b = b, a + b
7        return b