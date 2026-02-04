'''Sort Colors
Medium
Company Tags
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:

Input: nums = [1,0,1,2]

Output: [0,1,1,2]
Example 2:

Input: nums = [2,1,0]

Output: [0,1,2]
Constraints:

1 <= nums.length <= 300.
0 <= nums[i] <= 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?'''

#brute force
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
#time complexity: O(nlogn)
#space complexity: O(1)

#counting sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1
#time complexity: O(n)
#space complexity: O(1)






