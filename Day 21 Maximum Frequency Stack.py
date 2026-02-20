'''Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
Example 1:

Input: ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]

Output: [null, null, null, null, null, null, null, 5, 7, 5, 4]
Explanation:
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop(); // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop(); // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop(); // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop(); // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Constraints:

0 <= val <= 1,000,000,000
At most 20,000 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.'''

#brute force:
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int) #dictionary to keep track of the frequency of each element in the stack
        self.stack = [] #list to represent the stack
        

    def push(self, val: int) -> None:
        self.stack.append(val) #push the value onto the stack
        self.cnt[val] += 1 #increment the frequency count for the value
        

    def pop(self) -> int:
        max_freq = max(self.cnt.values())
        i = len(self.stack) - 1
        while self.cnt[self.stack[i]] != max_freq:
            i -= 1
        self.cnt[self.stack[i]] -= 1
        return self.stack.pop(i)
#time complexity: O(n) for the pop operation, where n is the number of elements in the stack, O(1) for the push operation
#space complexity: O(n) for the stack and the frequency dictionary