neighbors = [[1,0], [-1,0], [0,1], [0,-1]]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 2: continue
                if any(0 <= i+neighbor[0] < len(grid) and 0 <= j+neighbor[1] < len(grid[i+neighbor[0]]) and grid[i+neighbor[0]][j+neighbor[1]] > 0 for neighbor in neighbors):
                    queue.append((i, j, minutes))
                    visited.add((i, j))
        while queue:
            next_row, next_col, next_minutes = queue.popleft()
            minutes = bfs(grid, queue, visited, next_row, next_col, next_minutes)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return minutes


def bfs(grid: List[List[int]], queue: deque, visited: set, row: int, col: int, minutes: int) -> int:
    match grid[row][col]:
        case 0:
            return minutes
        case 1:
            grid[row][col] = 2
        case _:
            pass
    
    mins = minutes
    for neighbor in neighbors:
        coords = [sum(x) for x in zip([row, col], neighbor)]
        if 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[coords[0]]) and grid[coords[0]][coords[1]] == 1 and (coords[0], coords[1]) not in visited:
            queue.append((coords[0], coords[1], minutes+1))
            visited.add((coords[0], coords[1]))

    if queue:
        next_row, next_col, next_minutes = queue.popleft()
        mins = bfs(grid, queue, visited, next_row, next_col, next_minutes)
    return mins