'''Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
'''
#brute force
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp):
            self.stack.append(tmp.pop())
        
        return mini
    #time complexity: O(n) for getMin() and O(1) for push(), pop() and top()
    #space complexity: O(n) for getMin() and O(1) for other functions


#two stacks:
class MinStack:

    def __init__(self):
        self.stack = [] #main stack to store all the elements
        self.minStack = [] #stack to store the minimum element at each level of the main stack

    def push(self, val: int) -> None:
        self.stack.append(val) #push the value to the main stack
        val = min(val, self.minStack[-1] if self.minSStack else val) #compare the value with the current minimum and push the smaller one to the minStack
        self.minStack.append(val) #push the minimum value to the minStack
        

    def pop(self) -> None:
        self.stack.pop() #pop the top element from the main stack
        self.minStack.pop() #pop the top element from the minStack to maintain the correct minimum value for the remaining elements in the main stack

    def top(self) -> int:
        return self.stack[-1] #return the top element of the main stack
        

    def getMin(self) -> int:
        return self.minStack[-1] #return the top element of the minStack which is the minimum element in the main stack
    #time complexity: O(1) for all functions
    #space complexity: O(n) for the two stacks in the worst case when all elements are in increasing order and O(1) when all elements are the same.