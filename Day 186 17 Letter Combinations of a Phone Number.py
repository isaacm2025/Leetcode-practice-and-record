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
2 <= digits[i] <= 9'''

#backtracking
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        def backtrack(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            for c in digitMap[digits[i]]:
                backtrack(i + 1, path + c)
        if digits:
            backtrack(0, "")
        return res
#time complexity: O(N * 4^M) where N is the length of the digits string and M is the maximum number of letters that can be mapped to a digit (which is 4 for digit '7' and '9')
#space complexity: O(N * 4^M) because we store all possible combinations in the result list and the recursion stack can go up to N in depth