# Last updated: 8/3/2025, 9:02:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return -1

        queue = deque([root])
        total = 0
        
        while queue:
            _len = len(queue)

            for i in range(_len):
                curr_node = queue.popleft()
                if low <= curr_node.val <= high:
                    total += curr_node.val
                
                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)
            
        return total
