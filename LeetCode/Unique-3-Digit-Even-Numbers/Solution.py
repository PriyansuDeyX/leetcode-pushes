1from collections import Counter
2
3class Solution:
4    def totalNumbers(self, digits: list[int]) -> int:
5        digit_count = Counter(digits)
6        distinct_even_numbers = 0
7        
8        for num in range(100, 1000, 2):
9            hundreds = num // 100
10            tens = (num // 10) % 10
11            units = num % 10
12            
13            num_count = Counter([hundreds, tens, units])
14            
15            possible = True
16            for digit, count in num_count.items():
17                if digit_count[digit] < count:
18                    possible = False
19                    break
20                    
21            if possible:
22                distinct_even_numbers += 1
23                
24        return distinct_even_numbers