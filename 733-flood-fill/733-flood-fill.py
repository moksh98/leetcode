# import numpy as np
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m = len(image)
#         n = len(image[0])
#         def dfs(image, sr, sc, old_color, color, visited):
#             if sr > m-1 or sc > n-1 or sr < 0 or sc < 0:
#                 return
#             elif visited[sr][sc] == 1 or image[sr][sc] != old_color:
#                 return
#             else:
#                 visited[sr][sc] = 1
#                 image[sr][sc] = color
#                 dfs(image, sr+1, sc, old_color, color, visited)
#                 dfs(image, sr-1, sc, old_color, color, visited)
#                 dfs(image, sr, sc+1, old_color, color, visited)
#                 dfs(image, sr, sc-1, old_color, color, visited)
#         visited = np.zeros((m, n))
#         dfs(image, sr, sc, image[sr][sc], color, visited)
#         return image
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
        