1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        s_to_t = {}
4        t_to_s = {}
5        
6        for char_s, char_t in zip(s, t):
7            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
8               (char_t in t_to_s and t_to_s[char_t] != char_s):
9                return False
10            
11            s_to_t[char_s] = char_t
12            t_to_s[char_t] = char_s
13            
14        return True
15        