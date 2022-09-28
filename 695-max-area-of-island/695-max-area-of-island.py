class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            area = 0
            if grid[row][col] == 1:
                area += 1
                grid[row][col] = 0
                if row >= 1:
                    area += dfs(row-1, col)
                if row+1 < m: 
                    area += dfs(row+1, col)
                if col >= 1:
                    area += dfs(row, col-1)
                if col+1 < n:
                    area += dfs(row, col+1)
            return area
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                max_area = area if area > max_area else max_area
        return max_area