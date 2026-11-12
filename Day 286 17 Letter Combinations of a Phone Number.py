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

#iterative
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for digit in digits:
            tmp = []
            for curStr in res:
                for c in mapping[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res
#time complexity: O(3^n * 4^m)  n is the number of digits that map to 3 letters (2, 3, 4, 5, 6, 8) and m is the number of digits that map to 4 letters
#space complexity: O(3^n * 4^m)  for the result