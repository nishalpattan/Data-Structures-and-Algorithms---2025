# Last updated: 8/3/2025, 9:02:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        inorder_traversal = list()
        stack = list()
        prev_node = None
        min_diff = float("inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev_node:
                min_diff = min(min_diff, abs(prev_node.val - root.val))
            prev_node = root
            root = root.right
        return min_diff
        
        