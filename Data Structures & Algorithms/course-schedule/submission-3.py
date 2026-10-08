from enum import Enum

class NodeState(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        if not prerequisites: return True
        for i in range(numCourses):
            adj[i] = []
        for src, dst in prerequisites:
            adj[dst].append(src)

        visited = {}

        def dfs(src):
            if src in visited: 
                return visited[src] == NodeState.BLACK # if false, cycle detected
            visited[src] = NodeState.GRAY

            for adjdst in adj[src]:
                if not dfs(adjdst):
                    return False
            visited[src] = NodeState.BLACK
            return True

        for src, dst in adj.items(): 
            if not dfs(src): return False
        
        return True