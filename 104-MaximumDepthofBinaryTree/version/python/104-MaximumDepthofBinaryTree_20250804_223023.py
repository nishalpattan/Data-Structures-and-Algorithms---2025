# Last updated: 8/4/2025, 10:30:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        max_depth = float("-inf")
        queue = deque([(root, 0)])
        while queue:
            curr_node, curr_depth = queue.popleft()
            if curr_depth > max_depth:
                max_depth = curr_depth
            if curr_node.left:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth + 1))
        return max_depth + 1