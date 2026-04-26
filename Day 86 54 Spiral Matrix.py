class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        def dfs(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return
            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
            dfs(col, row - 1, r, c, dc, -dr)
        dfs(n,m, 0, -1, 0, 1)
        return res
#time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix. This is because we need to visit each element of the matrix once to add it to the result list.
#space complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix. This is because we are storing the result in a list that can potentially contain all elements of the matrix. Additionally, the recursive call stack can go as deep as O(min(m, n)) in the worst case, but this is overshadowed by the space used for the result list.

#optimal iterative solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]
        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res
#time complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix. This is because we need to visit each element of the matrix once to add it to the result list.
#space complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix. This is because we are storing the result in a list that can potentially contain all elements of the matrix. The additional space used for the directions and steps lists is negligible compared to the space used for the result list.