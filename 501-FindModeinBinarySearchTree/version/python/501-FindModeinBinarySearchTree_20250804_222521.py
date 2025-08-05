# Last updated: 8/4/2025, 10:25:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None: return -1
        
        if k == 0: return -1

        # output = list()
        count = 0
        res = None
        def inorder_dfs(root):
            nonlocal count
            nonlocal res
            if root is None: return
            
            inorder_dfs(root.left)
            count += 1
            if count == k:
                res = root.val
                return
            inorder_dfs(root.right)
        inorder_dfs(root)
        return res
        