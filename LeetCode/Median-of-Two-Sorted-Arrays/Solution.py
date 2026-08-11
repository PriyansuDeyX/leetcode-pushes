1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        merged = []
4        i = j = 0
5
6        while i < len(nums1) and j < len(nums2):
7            if nums1[i] < nums2[j]:
8                merged.append(nums1[i])
9                i += 1
10            else:
11                merged.append(nums2[j])
12                j += 1
13
14        while i < len(nums1):
15            merged.append(nums1[i])
16            i += 1
17
18        while j < len(nums2):
19            merged.append(nums2[j])
20            j += 1
21
22        n = len(merged)
23
24        if n % 2 == 1:
25            return float(merged[n // 2])
26
27        return (merged[n//2 - 1] + merged[n//2]) / 2