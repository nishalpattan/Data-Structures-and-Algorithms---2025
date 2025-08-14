# Last updated: 8/13/2025, 9:47:39 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        last = None
        start = head
        while start:
            _next = start.next
            start.next = last
            last = start
            start = _next
        return last 