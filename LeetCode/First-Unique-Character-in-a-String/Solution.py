1from collections import Counter
2class Solution:
3
4  def firstUniqChar(self, s: str) -> int:
5    counts = Counter(s)
6
7    for i, char in enumerate(s):
8      if counts[char] == 1:
9        return i
10
11    return -1