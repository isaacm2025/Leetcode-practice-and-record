'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2
Constraints:

1 <= nums.length <= 50,000
-1,000,000,000 <= nums[i] <= 1,000,000,000
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
from typing import List
#brute force approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) #length of nums
        for num in nums: #traverse through nums
            count = sum(1 for i in nums if i == num) #count occurrences of num
            if count > n // 2: #if count is greater than n/2
                return num #return num
#time complexity O(n^2)
#space complexity O(1)

#hashmap approach
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int) #dictionary to store counts
        res = max_count = 0 #initialize result and max_count

        for num in nums: #traverse through nums
            count[num] += 1 #increment count of num
            if max_count < count[num]: #if current count is greater than max_count
                res = num #update result
                max_count = count[num] #update max_count
        return res
#time complexity O(n)
#space complexity O(n)

#sorting approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() #sort the nums array
        return nums[len(nums) // 2] #return middle element
#time complexity O(n log n)
#space complexity O(1) if sorting in place

#bit manipulation approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) #length of nums
        bit = [0] * 32 #to store count of bits
        for num in nums: #traverse through nums
            for i in range(32): #for each bit position
                bit[i] += ((num>>i) & 1) #counting bits
        res = 0 #result variable
        for i in range(32): #traverse through bit counts
            if bit[i] > (n // 2): #if count of bits is greater than n/2
                if i == 31: #handling negative numbers
                    res -= (1 << i) #subtracting to get negative value
                else:
                    res += (1 << i) #adding to result
        return res 
#time complexity O(n)
#space complexity O(1) 

#Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0 #initialize result and count
        for num in nums: #traverse through nums
            if count == 0: #if count is zero
               res = num #set current number as result
            count += (1 if num == res else -1) #increment or decrement count
        return res
#time complexity O(n)
#space complexity O(1)

#randomization approach
import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) #length of nums
        while True: #infinite loop
            candidate = random.choice(nums) #randomly select a candidate
            if nums.count(candidate) > n // 2: #check if candidate is majority
                return candidate
#time complexity O(n) on average
#space complexity O(1)