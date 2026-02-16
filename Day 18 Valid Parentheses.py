'''You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000'''

#brute force 1
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: #we need to check if there are any valid pairs of brackets in the string
            s = s.replace('()', '') #if there are, we can remove them from the string using replace()
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == '' #if the string is empty after removing all valid pairs of brackets, 
                        # then it is a valid string, so we return True. Otherwise, we return False.
#time complexity: O(n^2) 
#because we are checking for valid pairs of brackets in the string and removing them until there are no more valid pairs left. 
#In the worst case, we may have to check the entire string multiple times, resulting in a time complexity of O(n^2).
#space complexity: O(n) because we are creating a new string each time we remove valid

#stack 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #to keep track of the opening brackets
        closeToOpen = {')': '(', '}': '{', ']': '['} #to map the closing brackets to their corresponding opening brackets

        for c in s:
            if c in closeToOpen: #if the character is a closing bracket, we need to check if it matches the top of the stack
                if stack and stack[-1] == closeToOpen[c]: #if the stack is not empty and the top of the stack matches the corresponding opening bracket, we can pop the top of the stack
                    stack.pop()
                else: #if the stack is empty or the top of the stack does not match the corresponding opening bracket, then the string is not valid, so we return False
                    return False
            else: #if the character is an opening bracket, we need to push it onto the stack
                stack.append(c)
        return True if not stack else False #if the stack is empty at the end, then the string is valid, so we return True. Otherwise, we return False.
#time complexity: O(n) because we are iterating through the string once and performing constant time operations for each character.
#space complexity: O(n) because in the worst case, we may have to push all opening brackets onto the stack, resulting in a space complexity of O(n).