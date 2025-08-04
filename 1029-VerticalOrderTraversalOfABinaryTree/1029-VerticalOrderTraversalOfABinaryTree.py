# Last updated: 8/3/2025, 9:02:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = collections.deque()
        q.append((root, 0,0))
        hash_map = dict()
        co_ordinates = list()
        while q:
            curr_node, row_idx, col_idx = q.popleft()
            co_ordinates.append((col_idx, row_idx, curr_node.val))
            if curr_node.left:
                q.append((curr_node.left, row_idx+1, col_idx-1))
            if curr_node.right:
                q.append((curr_node.right, row_idx+1, col_idx+1))
        co_ordinates.sort()
        for col, row, val in co_ordinates:
            if col in hash_map:
                hash_map[col].append(val)
            else:
                hash_map[col] = [val]
        return hash_map.values()
            