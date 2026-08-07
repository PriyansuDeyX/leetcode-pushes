1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7# Definition for singly-linked list.
8# class ListNode:
9#     def __init__(self, x):
10#         self.val = x
11#         self.next = None
12
13class Solution:
14    def hasCycle(self, head: Optional[ListNode]) -> bool:
15        slow = head
16        fast = head
17        
18        while fast and fast.next:
19            slow = slow.next
20            fast = fast.next.next
21            
22            if slow == fast:
23                return True
24                
25        return False