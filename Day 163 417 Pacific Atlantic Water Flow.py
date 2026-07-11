'''You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:



Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:

Input: heights = [[1],[1]]

Output: [[0,0],[1,0]]
Constraints:

1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000'''

#dfs
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c<0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
#time complexity: O(M * N) where M is the number of rows and N is the number of columns in the heights matrix. This is because we are performing a DFS from each cell in the matrix, and each cell can be visited at most once.
#space complexity: O(M * N) where M is the number of rows and N is the number of columns in the heights matrix. This is because we are using two sets to keep track of the cells that can reach the Pacific and Atlantic oceans, 
# and in the worst case, all cells can reach both oceans, so the space used by the sets can be proportional to the number of cells