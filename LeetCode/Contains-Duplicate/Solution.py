1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4        for num in nums:
5            if num in seen:
6                return True
7            seen.add(num)
8        return False