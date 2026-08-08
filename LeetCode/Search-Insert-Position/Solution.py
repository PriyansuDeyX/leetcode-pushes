1class Solution:
2
3  def searchInsert(self, nums: list[int], target: int) -> int:
4    left, right = 0, len(nums) - 1
5
6    while left <= right:
7      mid = (left + right) // 2
8
9      if nums[mid] == target:
10        return mid
11      elif nums[mid] < target:
12        left = mid + 1
13      else:
14        right = mid - 1
15
16    return left