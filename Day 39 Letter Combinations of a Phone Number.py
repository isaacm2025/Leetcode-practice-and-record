'''You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.



Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9'''

from typing import List
#backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitTochar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitTochar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, '')
        return res
#time complexity: O(n * 4^n) where n is the length of the input string digits. In the worst case, each digit can map to 4 characters (e.g., '7' and '9'), and we need to generate all possible combinations, which is 4^n. Additionally, we need to concatenate characters to form the current string, which takes O(n) time.
#space complexity: O(n) for the recursion stack and the temporary string used to build the current combination. The output list can also take up to O(4^n) space in the worst case, if all combinations are generated.
