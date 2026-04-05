'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
'''

from typing import List
#brute force
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i - 1])
                    if tokens[i] == "+":
                        tokens[i] = str(a + b)
                    elif tokens[i] == "-":
                        tokens[i] = str(a - b)
                    elif tokens[i] == "*":
                        tokens[i] = str(a * b)
                    else:
                        tokens[i] = str(int(a / b))
                    tokens.pop(i-1)
                    tokens.pop(i-2)
                    break
        return int(tokens[0])
#time complexity: O(n^2) where n is the number of tokens in the input list, O(n) for the while loop and O(n) for the for loop
#space complexity: O(1) since we are modifying the input list in place and not using any additional data structures