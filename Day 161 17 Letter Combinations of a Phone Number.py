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

#iteration
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
            temp = []
            for combination in res:
                for letter in mapping[digit]:
                    temp.append(combination + letter)
            res = temp
        return res
#time complexity: O(n * 4^m) where n is the length of the digits string and m is the maximum number of letters that a digit can map to (which is 4 for digits 7 and 9). In the worst case, we might explore all possible combinations of letters for each digit.
#space complexity: O(n* 4^m) for the result list, where m is the maximum number of letters that a digit can map to. In the worst case, we might store all possible combinations of letters for each digit.