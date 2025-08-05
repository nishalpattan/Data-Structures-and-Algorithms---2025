# Last updated: 8/4/2025, 5:37:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        

        def preorder(root, curr_sum):
            if root is None: return False

            curr_sum += root.val
            if curr_sum == targetSum and (root.left is None and root.right is None):
                return True            
            
            left_sum = preorder(root.left, curr_sum)
            right_sum = preorder(root.right, curr_sum)
            return left_sum or right_sum
        return preorder(root, 0)

        return preorder(root, 0)
