1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4
5        pairs = {
6            ')': '(',
7            '}': '{',
8            ']': '['
9        }
10
11        for ch in s:
12            if ch in "({[":
13                stack.append(ch)
14            else:
15                if not stack or stack.pop() != pairs[ch]:
16                    return False
17
18        return len(stack) == 0