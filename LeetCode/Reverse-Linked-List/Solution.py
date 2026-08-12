1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        prev = None
10        curr = head
11        
12        while curr:
13            next_node = curr.next  # 1. Store next node
14            curr.next = prev       # 2. Reverse pointer direction
15            prev = curr            # 3. Move prev one step forward
16            curr = next_node       # 4. Move curr one step forward
17            
18        return prev