1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        total_degree = 0
4        for i, char in enumerate(s):
5            str_pos = i + 1
6            rev_alpha_pos = 26 - (ord(char) - ord('a'))
7            total_degree += rev_alpha_pos * str_pos
8        return total_degree