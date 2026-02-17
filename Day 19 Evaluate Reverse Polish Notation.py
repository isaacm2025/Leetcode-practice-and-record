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
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
'''
#brute force:
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1: #we want to keep evaluating the expression until we have one final result
            for i in range(len(tokens)): #we want to iterate through the tokens list and find the first operator we encounter
                if tokens[i] in "+-*/": #if we find an operator, we want to perform the operation on the two operands that come before it
                    a = int(tokens[i-2]) #we want to convert the operands from strings to integers so we can perform the operation on them
                    b = int(tokens[i-1])#we want to convert the operands from strings to integers so we can perform the operation on them
                    if tokens[i] == '+': #if the operator is addition, we want to add the two operands together
                        result = a + b #we want to store the result of the operation in a variable so we can replace the operator and operands with the result in the tokens list
                    elif tokens[i] == '-': 
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:] #we want to replace the operator and operands with the result in the tokens list so we can continue evaluating the expression until we have one final result
                    break #we want to break out of the loop after we perform the operation so we can start iterating through the tokens list again from the beginning to find the next operator
        return int(tokens[0]) #we want to return the final result of the expression, which will be the only element left in the tokens list after we have evaluated the entire expression
    #time complexity: O(n^2) because we are iterating through the tokens list and performing operations on it
    #space complexity: O(n) because we are creating a new list of tokens every time we perform an operation

#recursion:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop() #we want to pop the last element from the tokens list because we want to evaluate the expression from the end to the beginning, since it's in reverse polish notation
            if token in "+-*/":
                return int(token)
            
            right = dfs() #we want to evaluate the right operand first because in reverse polish notation, the operator comes after the operands, so we want to evaluate the right operand before the left operand
            left = dfs() #we want to evaluate the left operand after we have evaluated the right operand because in reverse polish notation, the operator comes after the operands, so we want to evaluate the left operand after the right operand

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return int(left * right)
            elif token == '/':
                return int(left / right)
        return dfs() #we want to call the dfs function to start evaluating the expression from the end to the beginning, since it's in reverse polish notation
    #time complexity: O(n) because we are iterating through the tokens list once
    #space complexity: O(n) because we are using a recursive stack to evaluate the expression
    
