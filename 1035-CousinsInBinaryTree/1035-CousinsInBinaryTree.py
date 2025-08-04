# Last updated: 8/3/2025, 9:02:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        check if both x and y have different parents and they are in same depth
        
        using queue / bfs store x,y node's parent and depth
        
        q : [(1, None, 0)] hash_map = {}
        q : [(2, 1, 1), (3, 1, 1)] hash_map = {}
        q : [(4, 2, 2)] hash_map = { 3 : (1 , 1)}
        q : [] hash_map = {3: (1,1) ; 4 : (2,2)}
        
        hash_map[x][0] != hash_map[y][0] and hash_map[x][1] == hash_map[y][1]
        TC : O(N) ; SC : O(N)
        """
        if root is None:
            return False
        q = collections.deque()
        q.append( (root, None, 0) )
        hash_map = dict()
        while q:
            curr_node, parent_node, depth = q.popleft()
            if curr_node.val == x:
                hash_map[x] = (parent_node, depth)
            elif curr_node.val == y:
                hash_map[y] = (parent_node, depth)
            
            if curr_node.left:
                q.append((curr_node.left, curr_node, depth + 1 ))
            
            if curr_node.right:
                q.append((curr_node.right, curr_node, depth + 1 ))
        if hash_map[x][0] != hash_map[y][0] and hash_map[x][1] == hash_map[y][1]:
            return True
        return False