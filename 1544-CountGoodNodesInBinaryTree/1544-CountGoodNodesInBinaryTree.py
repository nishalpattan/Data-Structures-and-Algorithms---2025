# Last updated: 8/3/2025, 9:01:58 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        if root is None:
            return 0
        q = collections.deque()
        q.append((root, -math.inf))
        while q:
            curr_node, curr_max = q.popleft()
            if curr_node.val >= curr_max:
                curr_max = curr_node.val
                good_nodes += 1
            if curr_node.left:
                q.append((curr_node.left, curr_max))
            if curr_node.right:
                q.append((curr_node.right, curr_max))
        return good_nodes
                