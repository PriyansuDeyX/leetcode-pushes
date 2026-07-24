1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3
4        n = len(haystack)
5        m = len(needle)
6
7        # Check every possible starting position
8        for i in range(n - m + 1):
9
10            match = True
11
12            # Compare characters
13            for j in range(m):
14                if haystack[i + j] != needle[j]:
15                    match = False
16                    break
17
18            if match:
19                return i
20
21        return -1