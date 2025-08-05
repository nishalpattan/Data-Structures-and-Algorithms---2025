# Last updated: 8/4/2025, 10:15:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        mode = list()
        hash_map = defaultdict(int)

        def inorder(root):
            if root is None: return

            inorder(root.left)
            curr_val = root.val
            hash_map[curr_val] += 1
            inorder(root.right)
        inorder(root)
        max_freq = max(hash_map.values())
        for key, val in hash_map.items():
            if hash_map[key] == max_freq:
                mode.append(key)
        return mode


        