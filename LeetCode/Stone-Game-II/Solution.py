1class Solution:
2    def stoneGameII(self, piles: list[int]) -> int:
3        n = len(piles)
4        
5        # Precompute suffix sums
6        suffix_sum = [0] * (n + 1)
7        for i in range(n - 1, -1, -1):
8            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
9            
10        memo = {}
11        
12        def solve(i: int, M: int) -> int:
13            # If current player can take all remaining piles
14            if i + 2 * M >= n:
15                return suffix_sum[i]
16            
17            if (i, M) in memo:
18                return memo[(i, M)]
19            
20            max_stones = 0
21            # Try taking X piles where 1 <= X <= 2M
22            for X in range(1, 2 * M + 1):
23                next_M = max(M, X)
24                # Current player gets total remaining minus opponent's best outcome
25                stones = suffix_sum[i] - solve(i + X, next_M)
26                max_stones = max(max_stones, stones)
27                
28            memo[(i, M)] = max_stones
29            return max_stones
30        
31        return solve(0, 1)