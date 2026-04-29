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
#time complexity: O(n^2) where n is the length of the input array
#space complexity: O(1)

#hashset
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return list(s)[0]
#time complexity: O(n) where n is the length of the input array
#space complexity: O(n) where n is the number of unique elements in the input array

#sorting
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]
#time complexity: O(n log n) where n is the length of the input array due to sorting
#space complexity: O(1) or O(n) depending on the sorting algorithm used

