1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        # Filter out non-alphanumeric characters and convert to lowercase
4        filtered = ''.join(char.lower() for char in s if char.isalnum())
5        
6        # Check if the filtered string equals its reverse
7        return filtered == filtered[::-1]