1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        stack = []
4        for char in s:
5            if char == ')':
6                temp = []
7                # Pop until we find the matching opening parenthesis
8                while stack and stack[-1] != '(':
9                    temp.append(stack.pop())
10                # Remove the '(' from the stack
11                if stack and stack[-1] == '(':
12                    stack.pop()
13                # Push the reversed characters back into the stack
14                for c in temp:
15                    stack.append(c)
16            else:
17                stack.append(char)
18                
19        return "".join(stack)