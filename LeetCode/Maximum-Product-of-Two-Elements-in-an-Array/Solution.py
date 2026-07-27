1class Solution:
2    def maxProduct(self, nums: list[int]) -> int:
3        max1 = max2 = 0
4        
5        for num in nums:
6            if num > max1:
7                max2 = max1
8                max1 = num
9            elif num > max2:
10                max2 = num
11                
12        return (max1 - 1) * (max2 - 1)