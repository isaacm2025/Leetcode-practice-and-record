'''You are given an encoded string s, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. There will not be input like 3a, 2[4], a[a] or a[2].

The test cases are generated so that the length of the output will never exceed 100,000.

Example 1:

Input: s = "2[a3[b]]c"

Output: "abbbabbbc"
Example 2:

Input: s = "axb3[z]4[c]"

Output: "axbzzzcccc"
Example 3:

Input: s = "ab2[c]3[d]1[x]"

Output: "abccdddx"
Constraints:

1 <= s.length <= 30
s is made up of lowercase English letters, digits, and square brackets '[]'.
All the integers in s are in the range [1, 300].
s is guaranteed to be a valid input.
'''
#recursion:
class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0 #pointer to keep track of the current index in the input string

        def helper():
            res = ""
            k = 0 #variable to keep track of the current number being processed

            while self.i < len(s):
                c = s[self.i] #current character being processed

                if c.isdigit():
                    k = k * 10 + int(c) #update k by multiplying the previous value by 10 and adding the new digit
                elif c == "[": #when we encounter an opening bracket, we need to recursively call the helper function to decode the substring inside the brackets
                    self.ii += 1 #move the pointer to the next character after the opening bracket
                    res += helper() * k #decode the substring and repeat it k times, then add it to the result
                    k = 0
                elif c == "]":
                    return res
                else:
                    res += c
                self.i += 1
            return res
        return helper()
#time complexity: O(n + N) n is the length of the input string and N is the length of the output string
#space complexity: O(n + N)

#stack:
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]": #if the current character is not a closing bracket, we simply push it onto the stack
                stack.append(s[i]) #push the current character onto the stack
            else:
                sub = ""
                while stack[-1] != "[": #when we encounter a closing bracket, we need to pop characters from the stack until we find the corresponding opening bracket, and concatenate them to form the substring that needs to be repeated
                    sub = stack.pop() + sub #pop the top character from the stack and add it to the front of the substring
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit(): #after we have the substring, we need to pop characters from the stack until we find a non-digit character, and concatenate them to form the number k that indicates how many times the substring should be repeated
                    k = stack.pop() + k #pop the top character from the stack and add it to the front of k
                stack.append(int(k) * sub) #repeat the substring k times and push it back onto the stack
        return "".join(stack)
#time complexity: O(n + N^2) n is the length of the input string and N is the length of the output string
#space complexity: O(n + N)

#two stack:
class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit(): #if the current character is a digit, we need to update k by multiplying the previous value by 10 and adding the new digit, this is because the number k can have multiple digits, for example "12[a]" means we need to repeat "a" 12 times, so we need to keep track of the previous value of k and update it accordingly
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                cur = string_stack.pop() + cur * count_stack.pop() #when we encounter a closing bracket, we need to pop the last string from the string stack and the last count from the count stack, and concatenate the current string repeated by the count to the popped string, then update cur to this new string
            else:
                cur += c
        return cur
#time complexity: O(n + N) n is the length of the input string and N is the length of the output string
#space complexity: O(n + N)