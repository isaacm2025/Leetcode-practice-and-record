'''
You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,4,1,2]

Output: [1,4,1,2,1,4,1,2]
Example 2:

Input: nums = [22,21,20,1]

Output: [22,21,20,1,22,21,20,1]
Constraints:

1 <= nums.length <= 1000.
1 <= nums[i] <= 1000
'''
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2): #two times
            for n in nums:
                ans.append(n)
        return ans
    
#if three concatenation 121, 121, 121
#O(n) time complexity
#The runtime grows linearly with the size of the input.
'''
n = length of nums

You loop through the array once

If nums has:

5 elements → ~5 operations

1,000 elements → ~1,000 operations
'''

#O(n) space complexity

'''
What it means:
The amount of extra memory used grows linearly with the input size.

In this problem

You create a new array ans of size 2n

Memory used depends on n

Even though it’s 2n, we drop constants in Big-O:

O(2n) → O(n)
'''

'''Imagine nums is a line of people:

Time O(n) → you look at each person once

Space O(n) → you build another line of the same size'''



class Solution:
    def getConcatenation(self, nums: List[int], x) -> List[int]:
        ans = [] #to store the concatenated array

        for i in range(x): #we can use a variable x to determine how many times we want to concatenate the array
            for n in nums: #we can iterate through the nums array and append each element to the ans array
                ans.append(n) #we can use the append() method to add elements to the end of the ans array
        return ans  #we can return the ans array after concatenating it x times

'''“The algorithm iterates through the array once, so the time complexity is O(n).
We also create a new array proportional to the input size, so the space complexity is O(n).”'''