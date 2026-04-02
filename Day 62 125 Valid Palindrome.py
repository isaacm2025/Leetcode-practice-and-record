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

#reverse String
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = " "
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
#time complexity is O(n) and space complexity is O(n)

#two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.alphanumeric(s[left]):
                left += 1
            while left < right and not self.alphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
    def alphanumeric(self, c):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9'))
#time complexity is O(n) and space complexity is O(1)