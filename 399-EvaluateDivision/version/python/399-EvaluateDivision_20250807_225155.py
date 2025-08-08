# Last updated: 8/7/2025, 10:51:55 PM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = list()
         
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()
            visited.add(start)
    
            while queue:
                curr_node, curr_weight = queue.popleft()
                if curr_node not in graph:
                    return -1.0
                if curr_node == end:
                    return curr_weight
                for nei in graph[curr_node]:
                    if nei[0] not in graph:
                        return -1.0
                    if nei[0] not in visited:
                        queue.append((nei[0], curr_weight * nei[1]))
                        visited.add(nei[0])
            return -1.0
          
        for idx, equation in enumerate(equations):
            _to = equation[0]
            _from = equation[1]
            weight = values[idx]
            graph[_to].append((_from, weight))
            graph[_from].append((_to, 1/weight))

    
        for idx, query in enumerate(queries):
            res.append(bfs(query[0], query[1]))
        return res