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
        self.i = 0

        def helper():
            res = ""
            k = 0

            while self.i < len(s):
                c = s[self.i]

                if c.isdigit():
                    k = k * 10 + int(c)
                elif c == "[":
                    self.ii += 1
                    res += helper() * k 
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
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * sub)
        return "".join(stack)
#time complexity: O(n + N^2) n is the length of the input string and N is the length of the output string
#space complexity: O(n + N)

