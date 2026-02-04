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

#three pointers 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
#time complexity: O(n)
# space complexity: O(1)

#three pointers 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        zero = one = two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two] = 2
                nums[one] = 1
                nums[zero] = 0
                zero += 1
                one += 1
                two += 1
            elif nums[i] == 1:
                nums[two] = 2
                nums[one] = 1
                one += 1
                two += 1
            else:
                nums[two] = 2
                two += 1
#time complexity: O(n)
#space complexity: O(1)

#three pointers 3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = one = 0
        for two in range(len(nums)):
            temp = nums[two]
            nums[two] = 2
            if temp < 2:
                nums[one] = 1
                one += 1
            if temp < 1:
                nums[zero] = 0
                zero += 1
#time complexity: O(n)
#space complexity: O(1)





