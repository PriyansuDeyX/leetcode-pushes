1class Solution:
2
3  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
4    """Do not return anything, modify nums1 in-place instead."""
5    p1 = m - 1  # Pointer for valid elements in nums1
6    p2 = n - 1  # Pointer for nums2
7    p = m + n - 1  # Pointer for total write position in nums1
8
9    # Traverse backwards while there are still elements in nums2
10    while p2 >= 0:
11      if p1 >= 0 and nums1[p1] > nums2[p2]:
12        nums1[p] = nums1[p1]
13        p1 -= 1
14      else:
15        nums1[p] = nums2[p2]
16        p2 -= 1
17      p -= 1