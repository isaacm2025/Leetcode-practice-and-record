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
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].'''

#recursion
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token in "+-*/":
                b = dfs()
                a = dfs()
                if token == "+":
                    return a + b
                elif token == "-":
                    return a - b
                elif token == "*":
                    return a * b
                else:
                    return int(a / b)
            else:
                return int(token)
        return dfs()
#time complexity: O(n) where n is the length of the input array tokens. We iterate through the array once, and each element is processed once.
#space complexity: O(n) where n is the length of the input array tokens. The recursion stack can go as deep as the number of elements in the array.