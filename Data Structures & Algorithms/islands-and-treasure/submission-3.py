from collections import deque

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: 
                    queue.append((i,j))
        d = 0
        while queue:
            i, j = queue.popleft()
            d = grid[i][j] + 1
            for ni, nj in neighbors:
                row = i+ni
                col = j+nj
                if 0 <= row < n and 0 <= col < m and grid[row][col] > d:
                    grid[row][col] = d
                    queue.append((row, col))