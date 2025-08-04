# Last updated: 8/3/2025, 9:02:36 PM
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        stack = list()
        op = list()
        for idx,point in enumerate(points):
            stack.append((idx,(((point[0] ** 2) + (point[1] ** 2)) ** 0.5)))
        stack.sort(key = lambda x : x[1])
        for idx,dist in stack[:K]:
            op.append(points[idx])
        return op
        