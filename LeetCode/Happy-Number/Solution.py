1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def get_next(number: int) -> int:
4            total_sum = 0
5            while number > 0:
6                number, digit = divmod(number, 10)
7                total_sum += digit ** 2
8            return total_sum
9
10        slow = n
11        fast = get_next(n)
12        
13        while fast != 1 and slow != fast:
14            slow = get_next(slow)
15            fast = get_next(get_next(fast))
16            
17        return fast == 1