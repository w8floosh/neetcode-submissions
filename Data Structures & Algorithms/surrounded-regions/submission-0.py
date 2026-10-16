neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        visited = set()
        exclude = dict()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if (i in [0, n-1] or j in [0, m-1]) and board[i][j] == "O": # start from the external ring
                    queue.append((i,j))
                    visited.add((i,j))
                    exclude[(i,j)] = True
        
        def BFS(i, j):
            for (ni, nj) in neighbors:
                coords = (i+ni, j+nj)
                if (
                        0 <= coords[0] <= n-1 and 
                        0 <= coords[1] <= m-1 and 
                        board[coords[0]][coords[1]] == "O" and 
                        coords not in visited
                ):
                    queue.append(coords)
                    visited.add(coords)
                    exclude[coords] = True
            
            if queue:
                (qi, qj) = queue.popleft()
                BFS(qi, qj)

        
        while queue:
            (i, j) = queue.popleft()
            BFS(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and not exclude.get((i,j)):
                    board[i][j] = "X"
            