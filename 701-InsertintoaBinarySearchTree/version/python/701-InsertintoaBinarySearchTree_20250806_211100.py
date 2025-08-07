# Last updated: 8/6/2025, 9:11:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_node(root, val):
            if root is None:
                return TreeNode(val)
            if val < root.val:
                root.left = insert_node(root.left, val)
            else:
                root.right = insert_node(root.right, val)
            return root

        insert_node(root, val)
        return TreeNode(val) if root is None else root