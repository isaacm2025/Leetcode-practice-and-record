'''Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.'''

#reverse string
class Solution:
    def isPlaindrome(self, s: str) -> bool:
        newStr = ''
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]
#time complexity: O(n)
#space complexity: O(n)

#two pointer
class Solution:
    def isPlaindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
    def alphaNum(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9')) #this line means if the character is between A-Z or a-z or 0-9, then it is alphanumeric
#time complexity: O(n)
#space complexity: O(1)