1class Solution:
2    def countCommas(self, n: int) -> int:
3        total = 0
4        k = 1
5        while True:
6            L = 10 ** (3 * k)
7            R = min(n, 10 ** (3 * k + 3) - 1)
8            if L > n:
9                break
10            total += k * (R - L + 1)
11            k += 1
12        return total