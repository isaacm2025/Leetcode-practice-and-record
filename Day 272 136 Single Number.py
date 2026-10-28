'''You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with 
O
(
n
)
O(n) runtime complexity and use only 
O
(
1
)
O(1) extra space.

Example 1:

Input: nums = [3,2,3]

Output: 2
Example 2:

Input: nums = [7,6,6,7,8]

Output: 8
Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000'''

#bf
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            flag = True
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    flag = False
                    break
            if flag:
                return nums[i]
#time complexity: O(n^2)
#space complexity: O(1)


#hashset
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set() # create a set to store the numbers we have seen
        for num in nums:
            if num in seen:
                seen.remove(num) # remove the number if it is already in the set
            else:
                seen.add(num) # add the number to the set if it is not in the set
        return list(seen)[0] #return the only number left in the set
#time complexity: O(n)
#space complexity: O(n)

#sorting
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2 # skip the next number since it is a duplicate
            else:
                return nums[i] # return the number that is not a duplicate
        return nums[-1] # return the last number if it is not a duplicate
#time complexity: O(nlogn)
#space complexity: O(1)