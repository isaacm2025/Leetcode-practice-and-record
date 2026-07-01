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

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].'''

#recursion
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            right = dfs()
            left = dfs()
            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        return dfs() 
#time complexity: O(n)
#space complexity: O(n)

#stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                right, left = stack.pop(), stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[0]
#time complexity: O(n)
#space complexity: O(n)