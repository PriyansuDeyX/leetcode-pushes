1class Solution:
2    def resultArray(self, nums: list[int], k: int) -> list[int]:
3        ans = [0] * k
4        dp = [0] * k
5        
6        for num in nums:
7            new_dp = [0] * k
8            num_mod = num % k
9            new_dp[num_mod] += 1
10            
11            for r in range(k):
12                if dp[r] > 0:
13                    new_dp[(r * num_mod) % k] += dp[r]
14            
15            for r in range(k):
16                ans[r] += new_dp[r]
17                
18            dp = new_dp
19            
20        return ans