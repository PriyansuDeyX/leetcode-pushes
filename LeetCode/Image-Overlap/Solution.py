1class Solution:
2
3  def largestOverlap(
4      self, img1: List[List[int]], img2: List[List[int]]
5  ) -> int:
6    n = len(img1)
7    list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
8    list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
9
10    counts = collections.defaultdict(int)
11    for r1, c1 in list1:
12      for r2, c2 in list2:
13        counts[(r1 - r2, c1 - c2)] += 1
14
15    return max(counts.values()) if counts else 0