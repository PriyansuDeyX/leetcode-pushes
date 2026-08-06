1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        current = n
4        while True:
5            # Calculate the product of the digits
6            prod = 1
7            temp = current
8            has_zero = False
9            
10            while temp > 0:
11                digit = temp % 10
12                if digit == 0:
13                    has_zero = True
14                    break
15                prod *= digit
16                temp //= 10
17                
18            digit_product = 0 if has_zero else prod
19            
20            # Check if the digit product is divisible by t
21            if digit_product % t == 0:
22                return current
23            
24            current += 1