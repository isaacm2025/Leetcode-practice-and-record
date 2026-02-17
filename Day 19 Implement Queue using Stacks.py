'''Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
Example 1:

Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 1, 1, false]
Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

'''
#using two stacks(brute force)

class MyQueue:

    def __init__(self):
        self.stack1 = [] #to keep track of the elements in the queue
        self.stack2 = [] #to help us with the push operation
    

    def push(self, x: int) -> None:
        self.stack1.append(x) #we can add the new element to the top of stack1
        

    def pop(self) -> int:
        while len(self.stack1) > 1: #we need to move all the elements from stack1 to stack2 except the last element to get the front element of the queue
            self.stack2.append(self.stack1.pop()) #we can move the elements from stack1 to stack2 using pop() to get the top element of stack1
        res = self.stack1.pop() #we can pop the front element of the queue using pop() to get the top element of stack1
        while self.stack2: #we need to move all the elements back from stack2 to stack1 to maintain the order of the queue
            self.stack1.append(self.stack2.pop()) #we can move the elements from stack2 to stack1 using pop() to get the top element of stack2
        return res #we can return the front element of the queue
    def peek(self) -> int:
        while len(self.stack1) > 1: #we need to move all the elements from stack1 to stack2 except the last element to get the front element of the queue
            self.stack2.append(self.stack1.pop()) #we can move the elements from stack1 to stack2 using pop() to get the top element of stack1
        res = self.stack1[-1] #we can get the front element of the queue using stack1[-1] to get the top element of stack1
        while self.stack2: #we need to move all the elements back from stack2 to stack1 to maintain the order of the queue
            self.stack1.append(self.stack2.pop()) #we can move the elements from stack2 to stack1 using pop() to get the top element of stack2
        return res #we can return the front element of the queue

    def empty(self) -> bool:
        return not self.stack1 #we can check if the queue is empty by checking if stack1 is empty
#time complexity: O(n) for pop and peek, O(1) for initialize, push, and empty
#space complexity: O(n) because we are using two stacks to store the elements


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
