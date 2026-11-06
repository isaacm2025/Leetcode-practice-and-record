'''You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 10000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].
'''

#bf
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        res = a + b
                    elif tokens[i] == '-':
                        res = a - b
                    elif tokens[i] == '*':
                        res = a * b
                    else:
                        res = int(a / b)
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break
        return int(tokens[0])
#time complexity: O(n^2)
#space complexity: O(n)