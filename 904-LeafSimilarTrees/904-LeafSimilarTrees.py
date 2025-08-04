# Last updated: 8/3/2025, 9:02:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        inorder_1 = self.inorder(root1)
        inorder_2 = self.inorder(root2)
        print(inorder_1)
        print(inorder_2)
        return inorder_1 == inorder_2
    
    def inorder(self, root):
        stack = list()
        order = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.left is None and root.right is None:
                order.append(root.val)
            root = root.right
        return order