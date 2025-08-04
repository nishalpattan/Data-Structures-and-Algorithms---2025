# Last updated: 8/3/2025, 9:02:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Floy'd algo / slow, fast pointer  TC:O(n); SC: O(1)
        sp = head
        fp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        return sp
        # Approach : 2 TC:O(n) ; SC:O(n)
        if head is None:
            return head
        count = 0
        curr = head
        hash_map = dict()
        while curr:
            count += 1
            hash_map[count] = curr
            curr = curr.next
        return hash_map[(count // 2) + 1]