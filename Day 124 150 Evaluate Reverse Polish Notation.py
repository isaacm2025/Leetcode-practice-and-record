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

#recursive

from ast import List
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
#time O(n) because we traverse the tokens list once
#space O(n) because of the recursive call stack


#stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(float(left) / right))
            else:
                stack.append(int(char))
        return stack[0]
#time O(n) because we traverse the tokens list once
#space O(n) because in the worst case we could have all operands in the stack