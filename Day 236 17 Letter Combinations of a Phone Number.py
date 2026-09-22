'''You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.

Phone keypad letter mapping

Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9
'''

#backtracking
from typing import List
class Solution:
    def letterCom(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
        if digits:
            dfs(0, "")
        return res
#time complexity: O(n * 4^n) where n is the length of the digits. In the worst case, we might explore all 4 possible characters for each digit in the input string.
#space complexity: O(n) where n is the length of the digits.