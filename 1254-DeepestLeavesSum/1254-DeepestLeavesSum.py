# Last updated: 8/3/2025, 9:02:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = collections.deque()
        q.append(root)
        depth = 0
        deep_sum = 0
        while q:
            size = len(q)
            depth += 1
            curr_sum = 0
            for i in range(size):
                curr_node = q.popleft()
                if curr_node.left is None and curr_node.right is None:
                    curr_sum += curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            deep_sum = curr_sum
        return deep_sum