'''Contains Duplicate
Easy
Company Tags
Hints
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''

'''1, 2, 3, 1; compare every element with every other element
Brute force: O(n^2) time complexity, n = length of nums


space complexity O(1), dont need any extra space/memory
'''
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): #loop through each element
            for j in range(i+1, len(nums)): #compare with every other element
                if nums[i] == nums[j]: #if number i and number j are the same
                    return True #duplicate found
        return False #no duplicates found
    


'''second approach: sorting
1, 1, 2, 3

we can see duplicate elements are adjacent
compare each element with the next one
O(n log n) time complexity due to sorting
O(1) space complexity if sorting in place
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sort the array
        for i in range(1, len(nums)): #start from index 1 to compare with previous element
            if nums[i] == nums[i - 1]: #if current element is same as previous element
                return True #duplicate found
        return False #no duplicates found
    
'''third approach: use extra memory and hash set, insert elements into the hashest in big O(n) time complexity
O(n) time complexity
O(n) space complexity
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #hash set
        for num in nums:
            if num in seen: #run through the set to check if the element is already present
                return True # True if duplicate found, False if not
            seen.add(num)   #add the element to the set
        return False # no duplicates found

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) #set(nums) removes duplicates from nums
    
'''set(nums) removes duplicates from nums
compare lengths: len(nums) and len(set(nums))
if lengths are different, duplicates were present in nums
if lengths are the same, no duplicates existed, return False'''



'''To detect duplicates efficiently, we need a data structure that:

Remembers what we’ve already seen

Can check quickly if something exists

 That structure is a set

 What is a set?

A set:

Stores unique values only

Automatically removes duplicates

Has O(1) average lookup time'''