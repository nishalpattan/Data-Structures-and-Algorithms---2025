# Last updated: 8/4/2025, 6:02:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: return []
        res = list()

        def dfs_backtrack(root, path, curr_sum):
            if root is None: return

            curr_sum += root.val
            path.append(root.val)

            if curr_sum == targetSum and root.left is None and root.right is None:
                res.append(path.copy())
                 
            dfs_backtrack(root.left, path, curr_sum)
            dfs_backtrack(root.right, path, curr_sum)
            path.pop()
        
        dfs_backtrack(root, [], 0)
        return res