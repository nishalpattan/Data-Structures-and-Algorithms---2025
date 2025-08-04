# Last updated: 8/3/2025, 9:02:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0
        res = 0
        curr = head
        while curr:
            res = (res * 2) + curr.val
            curr = curr.next
        return res