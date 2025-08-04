# Last updated: 8/3/2025, 9:24:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        res=list()
        while q:
            size = len(q)
            for i in range(size):
                curr_node = q.popleft()
                if i == size - 1:
                    res.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return res