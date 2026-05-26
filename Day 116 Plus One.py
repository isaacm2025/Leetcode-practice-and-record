'''You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9'''

#recursion
from typing import List
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
#time complexity: O(n), where n is the number of digits in the input list, due to the recursive calls and the operations performed on the digits.
#space complexity: O(n), where n is the number of digits in the input list, due to the space used for the recursive call stack and the new list created during the recursion.

#iteration
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
#time complexity: O(n), where n is the number of digits in the input list, due to the loop that iterates through the digits.
#space complexity: O(n), where n is the number of digits in the input list, due to the in-place modification of the input list and the constant space used for the new list when all digits are 9.