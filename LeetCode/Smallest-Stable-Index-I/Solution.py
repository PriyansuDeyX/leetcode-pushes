1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        
5        # Compute suffix minimums
6        suff_min = [0] * n
7        suff_min[-1] = nums[-1]
8        for i in range(n - 2, -1, -1):
9            suff_min[i] = min(nums[i], suff_min[i + 1])
10            
11        # Track running prefix maximum and check stability
12        curr_max = nums[0]
13        for i in range(n):
14            curr_max = max(curr_max, nums[i])
15            instability_score = curr_max - suff_min[i]
16            
17            if instability_score <= k:
18                return i
19                
20        return -1