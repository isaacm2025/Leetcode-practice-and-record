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
At most 
3
∗
10
4
3∗10 
4
  calls will be made to push, pop, top, and getMin.'''

#bf
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
        while len(self.stack) > 0:
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        while len(tmp) > 0:
            self.stack.append(tmp.pop())
        return mini
#time complexity: O(n) where n is the number of elements in the stack. The getMin function iterates through the entire stack to find the minimum element.
#space complexity: O(n) where n is the number of elements in the stack. We use an additional stack to store the elements while finding the minimum element.

#two stacks
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
#time complexity: O(1) for all operations. Each operation (push, pop, top, getMin) takes constant time.
#space complexity: O(n) where n is the number of elements in the stack. We use an additional stack to store the minimum elements, which can contain at most n elements in the worst case.