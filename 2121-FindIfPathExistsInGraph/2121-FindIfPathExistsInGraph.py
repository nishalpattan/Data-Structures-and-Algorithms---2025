# Last updated: 8/3/2025, 9:01:54 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        # I will convert to adjacency list

        adjacencyList = defaultdict(list)

        for v1, v2 in edges:
            if v1 not in adjacencyList:
                adjacencyList[v1] = []
            if v2 not in adjacencyList:
                adjacencyList[v2] = []

            adjacencyList[v1].append(v2)
            adjacencyList[v2].append(v1)

        # use bfs algorithm starting from the source node provided in the input
        # add the source node to the queue
        queue = deque([source])
        visited.add(source)
        while queue:
                # pop the queue if the node is target return true
                curr_node = queue.popleft()
                if curr_node == destination:
                    return True
                # else get the neighbors of the node, add to the queue
                for neighbor in adjacencyList[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

                # add node to the visited node list
        return False
        