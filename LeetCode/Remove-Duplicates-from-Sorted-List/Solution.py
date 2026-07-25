1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class ListNode:
7    def __init__(self, val=0, next=None):
8        self.val = val
9        self.next = next
10
11class Solution:
12    def deleteDuplicates(self, head: ListNode) -> ListNode:
13        current = head
14        
15        while current and current.next:
16            if current.val == current.next.val:
17                # Skipping the duplicate node (hataate hobe jegulo dupli ache)
18                current.next = current.next.next
19            else:
20                # Move to the next non same element
21                current = current.next
22                
23        return head