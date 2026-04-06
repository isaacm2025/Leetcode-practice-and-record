'''You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000'''


from typing import List
#brute force
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
#time complexity: O(m * n) where m is the number of rows and n is the number of columns, we are iterating through each element in the matrix
#space complexity: O(1) since we are using a constant amount of space to store the target and the current element

#stairecase search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
#time complexity: O(m + n) where m is the number of rows and n is the number of columns, in the worst case we will have to iterate through all the rows and columns
#space complexity: O(1) since we are using a constant amount of space to store the target and the current element