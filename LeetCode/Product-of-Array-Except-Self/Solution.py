1from typing import List
2class Solution:
3    def productExceptSelf(self, nums: List[int]) -> List[int]:
4        n = len(nums)
5        answer = [1] * n
6        
7        # Pass 1: Calculate left products
8        left_product = 1
9        for i in range(n):
10            answer[i] = left_product
11            left_product *= nums[i]
12            
13        # Pass 2: Calculate right products and multiply on the fly
14        right_product = 1
15        for i in range(n - 1, -1, -1):
16            answer[i] *= right_product
17            right_product *= nums[i]
18            
19        return answer