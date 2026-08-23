1class Solution:
2    def sumGame(self, num: str) -> bool:
3        n = len(num)
4        half = n // 2
5        
6        s1 = sum(int(c) for c in num[:half] if c != '?')
7        s2 = sum(int(c) for c in num[half:] if c != '?')
8        
9        q1 = num[:half].count('?')
10        q2 = num[half:].count('?')
11        
12        if (q1 + q2) % 2 != 0:
13            return True
14            
15        return (s1 - s2) * 2 != (q2 - q1) * 9