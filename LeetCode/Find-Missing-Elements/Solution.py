1class Solution:
2    def findMissingElements(self, nums: list[int]) -> list[int]:
3        min_val = min(nums)
4        max_val = max(nums)
5        
6        num_set = set(nums)
7        missing = []
8        
9        for i in range(min_val + 1, max_val):
10            if i not in num_set:
11                missing.append(i)
12                
13        return missing
14        