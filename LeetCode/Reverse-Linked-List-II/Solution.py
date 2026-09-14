1class ListNode:
2    def __init__(self, val=0, next=None):
3        self.val = val
4        self.next = next
5
6class Solution:
7    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
8        if not head or left == right:
9            return head
10        
11        dummy = ListNode(0, head)
12        prev = dummy
13        
14        for _ in range(left - 1):
15            prev = prev.next
16            
17        curr = prev.next
18        for _ in range(right - left):
19            next_node = curr.next
20            curr.next = next_node.next
21            next_node.next = prev.next
22            prev.next = next_node
23            
24        return dummy.next