# Last updated: 8/3/2025, 9:16:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        output = list()
        queue = deque([root])

        while queue:
            _len = len(queue)
            temp = list()
            for i in range(_len):
                curr_node = queue.popleft()
                temp.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            output.append(temp[-1])
                
        return output
        