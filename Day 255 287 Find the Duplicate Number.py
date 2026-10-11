'''You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10,000
nums.length == n + 1
1 <= nums[i] <= n'''

#sorting
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return -1
#time complexity: O(nlogn)
#space complexity: O(1)

#hashset
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num) # add the number to the set
        return -1 #return -1 if no duplicate is found
#time complexity: O(n)
#space complexity: O(n)


#array
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums) # create an array of size n + 1, initialized with 0
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1
#time complexity: O(n)
#space complexity: O(n)

#two pointers
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow] #move slow pointer by one step, why need to use nums[slow]? because the value of the element at index slow is the next index to move to, why dont use slow.next? because the input is an array, not a linked list
            fast = nums[nums[fast]] #move fast pointer by two steps
            if slow == fast:
                break
        slow2 = 0 #initialize a new pointer slow2 to the start of the array
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow #return the value of the duplicate number
#time complexity: O(n)
#space complexity: O(1)