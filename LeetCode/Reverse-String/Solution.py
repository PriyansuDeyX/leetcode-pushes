1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        left, right = 0, len(s) - 1
7        
8        while left < right:
9            # Swap the characters
10            s[left], s[right] = s[right], s[left]
11            
12            # Move the pointers towards the center
13            left += 1
14            right -= 1