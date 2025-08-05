# Last updated: 8/4/2025, 9:32:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(left, right, level):
            if left is None: return

            if level%2 == 1:
                left.val, right.val = right.val, left.val
            
            
            dfs(left.left, right.right, level+1)
            dfs(left.right, right.left, level+1)
            
        dfs(root.left, root.right, 1)
        return root