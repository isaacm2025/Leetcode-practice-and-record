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
#brute force:
#class Solution:
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in range(len(matrix)): #iterate through the rows of the matrix
        for col in range(len(matrix[0])): #iterate through the columns of the matrix
            if matrix[row]][col] == target: #if the current element is equal to the target, return true
                return True
    return False
#time complexity: O(m*n)
#space complexity: O(1)

#staircase search:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) #the number of rows and columns in the matrix
        r, c = 0, n - 1 #start from the top right corner of the matrix
        while r < m and c >= 0:
            if matrix[r][c] > target: #if the current element is greater than the target, we need to search in the left half of the current row
                c -= 1
            elif matrix[r][c] < target: #if the current element is less than the target, we need to search in the right half of the current column
                r += 1
            else:
                return True
        return False
#time complexity: O(m+n)
#space complexity: O(1)

#Binary search one pass
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) #the number of rows and columns in the matrix
        left, right = 0, ROWS * COLS - 1 #the left and right pointers for the binary search
        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // COLS, mid % COLS
            if target > matrix[row][col]: #if the target is greater than the current element, we need to search in the right half of the current row
                left = mid + 1
            elif target < matrix[row][col]: #if the target is less than the current element, we need to search in the left half of the current row
                right = mid - 1
            else:
                return True
        return False
#time complexity: O(log(m*n))
#space complexity: O(1)