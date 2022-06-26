class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        good = {}
        bad = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bad.append((i, j))
                elif grid[i][j] == 1:
                    good[(i, j)] = (i, j)
        mins = -1
        temp = []
        if not good and not bad:
            return 0
        while len(bad) != 0:
            loc = bad.pop(0)
            row, col = loc[0], loc[1]
            if row+1 < m and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                del good[(row+1, col)]
                temp.append((row+1, col))
            if row >= 1 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                del good[(row-1, col)]
                temp.append((row-1, col))
            if col+1 < n and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                del good[(row, col+1)]
                temp.append((row, col+1))
            if col >= 1 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                del good[(row, col-1)]
                temp.append((row, col-1))
            if len(bad) == 0:
                mins += 1
                bad = temp
                temp = []
        if len(good) > 0:
            return -1
        else:
            return mins
            