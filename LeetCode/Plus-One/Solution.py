1class Solution:
2
3  def plusOne(self, digits: list[int]) -> list[int]:
4    n = len(digits)
5
6    # Traverse from right to left
7    for i in range(n - 1, -1, -1):
8      if digits[i] < 9:
9        digits[i] += 1
10        return digits
11
12      # If digit is 9, it becomes 0 and carry continues
13      digits[i] = 0
14
15    # If all digits were 9 (e.g., [9, 9, 9] -> [0, 0, 0]), prepend 1
16    return [1] + digits