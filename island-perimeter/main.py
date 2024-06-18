# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Seeing that perimiter = 4 (side) - landNumber
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for y in range(row):
            for x in range(col):
                if grid[y][x] == 1:
                    peri = 4
                    if y >= 1:
                        if grid[y-1][x] == 1:
                            peri -= 1
                    if x < col - 1:
                        if grid[y][x+1] == 1:
                            peri -= 1
                    if y < row - 1:
                        if grid[y+1][x] == 1:
                            peri -= 1
                    if x >= 1:
                        if grid[y][x-1] == 1:
                            peri -= 1
                    perimeter += peri
        # TIme: O(row * col)
        # Space: O(1)
        return perimeter
