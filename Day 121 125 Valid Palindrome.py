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
from ast import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum(): #isalnum() is a built-in method in Python that checks if a character is alphanumeric (i.e., a letter or a number)
                newStr += char.lower() #add the lowercase version of the character to the new string if it is alphanumeric
        return newStr == newStr[::-1] #return true if the new string is equal to its reverse, otherwise return false, where newStr[::-1] is a slicing operation that creates a new string that is the reverse of newStr.
#time O(n) because we need to iterate through the input string once to create the new string and then we need to compare the new string with its reverse, which takes O(n) time
#space O(n) because we create a new string to store the alphanumeric characters from the input string, which can contain at most n characters in the worst case.

