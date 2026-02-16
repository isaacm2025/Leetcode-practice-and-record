'''Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
Example 1:

Input: ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 2, 2, false]
Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
Follow-up: Can you implement the stack using only one queue?
'''
#using two queues
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque() #to keep track of the elements in the stack
        self.q2 = deque() #to help us with the push operation

    def push(self, x: int) -> None:
        self.q2.append(x) #we can add the new element to the back of q2
        while self.q1: #we need to move all the elements from q1 to q2 to maintain the order of the stack
            self.q2.append(self.q1.popleft()) #we can move the elements from q1 to q2 using popleft() to get the front element of q1
        self.q1, self.q2 = self.q2, self.q1 #we can swap q1 and q2 to make q1 the new stack and q2 the empty queue for the next push operation

    def pop(self) -> int:
        return self.q1.popleft() #we can pop the top element of the stack using popleft() to get the front element of q1

    def top(self) -> int:
        return self.q1[0] #we can get the top element of the stack using q1[0] to get the front element of q1

    def empty(self) -> bool:
        return len(self.q1) == 0 #we can check if the stack is empty by checking if q1 is empty
#time complexity: O(n) for push, O(1) for pop, top, and empty
#space complexity: O(n) because we are using two queues to store the elements


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#queue of queues:
class MyStack:

    def __init__(self):
        self.q = None #to keep track of the elements in the stack

    def push(self, x: int) -> None:
        self.q = deque([x, self.q]) #we can add the new element to the front of the queue and point it to the previous queue

    def pop(self) -> int:
        top = self.q.popleft() #we can pop the top element of the stack using popleft() to get the front element of the queue
        self.q = self.q.popleft() #we can update the queue to point to the next queue in the stack
        return top #we can return the popped element

    def top(self) -> int:
        return self.q[0] #we can get the top element of the stack using q[0] to get the front element of the queue  

    def empty(self) -> bool:
        return not self.q #we can check if the stack is empty by checking if the queue is empty
#time complexity: O(1) for push, pop, top, and empty
#space complexity: O(n) because we are using a queue of queues to store the elements