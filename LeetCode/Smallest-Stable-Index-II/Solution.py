1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        
5        suff_min = [0] * n
6        suff_min[-1] = nums[-1]
7        for i in range(n - 2, -1, -1):
8            suff_min[i] = min(nums[i], suff_min[i + 1])
9            
10        curr_max = nums[0]
11        for i in range(n):
12            curr_max = max(curr_max, nums[i])
13            if curr_max - suff_min[i] <= k:
14                return i
15                
16        return -1