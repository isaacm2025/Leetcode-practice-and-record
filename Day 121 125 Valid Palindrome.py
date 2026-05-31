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

#recursive
from ast import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(left, right):
            while left < right and not s[left].isalnum(): #if the left pointer is less than the right pointer and the character at the left pointer is not alphanumeric, 
                left += 1 #move the left pointer to the right
            while left < right and not s[right].isalnum():
                right -= 1 #move the right pointer to the left if the character at the right pointer is not alphanumeric
            if left >= right: #if the left pointer is greater than or equal to the right pointer, it means we have checked all the characters and they are all valid, so we can
                return True #return true for the base case of the recursion
            if s[left].lower() != s[right].lower(): #if the characters at the left and right pointers are not equal (ignoring case), it means the string is not a palindrome, so we can return false
                return False
            return helper(left + 1, right - 1) #if the characters at the left and right pointers are equal, we can move both pointers towards the center and continue checking the remaining characters by making a recursive call to the helper function with updated left and right pointers.
        return helper(0, len(s) - 1) #call the helper function with the initial left pointer at the start of the string and the right pointer at the end of the string to start the recursive checking process.
#time O(n) because in the worst case, we might have to check each character in the input string once, where n is the length of the input string.
#space O(n) because in the worst case, we might have to make n recursive calls to the helper function, where n is the length of the input string. Each recursive call adds a new frame to the call stack, which can take up to O(n) space in the worst case.