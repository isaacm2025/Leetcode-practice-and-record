'''You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

Note:

The order of the elements which are not equal to val does not matter.
It is not necessary to consider elements beyond the first k positions of the array.
To be accepted, the first k elements of nums must contain only elements not equal to val.
Return k as the final result.

Example 1:

Input: nums = [1,1,2,3,4], val = 1

Output: [2,3,4]
Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: [0,1,3,0,4]
Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''

#brute force approach
from ast import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = [] #to store elements not equal to val
        for num in nums: #traverse through nums
            if num == val: #if num is equal to val, skip it
                continue #continue to next iteration
            temp.append(num) #append num to tem if element is equal to val
        for i in range(len(temp)): #for loop to copy elements from temp to nums
            nums[i] = temp[i] #copying elements from temp to nums
        return len(temp) #return length of temp
#time complexity O(n)
#space complexity O(n)

#two pointer approach
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 #pointer for next position of non-val element
        for i in range(len(nums)): #traverse through nums
            if nums[i] != val: #if element is not equal to val
                nums[k] = nums[i] #copy element to position k
                k += 1 #increment k
        return k
#time complexity O(n)
#space complexity O(1)


#two pointer approach (two)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 #pointer for current element
        n = len(nums) #length of nums
        while i < n: #while i is less than n
            if nums[i] == val: #if current element is equal to val
                nums[i] = nums[n - 1] #replace it with last element
                n -= 1 #decrement n
            else:
                i += 1 #increment i
        return n
#time complexity O(n)
#space complexity O(1)