'''You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7,8], k = 4

Output: [5,6,7,8,1,2,3,4]
Explanation:
rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
rotate 4 steps to the right: [5,6,7,8,1,2,3,4]

Example 2:

Input: nums = [1000,2,4,-3], k = 2

Output: [4,-3,1000,2]
Explanation:
rotate 1 steps to the right: [-3,1000,2,4]
rotate 2 steps to the right: [4,-3,1000,2]

Constraints:

1 <= nums.length <= 100,000
-(2^31) <= nums[i] <= ((2^31)-1)
0 <= k <= 100,000
Follow up: Could you do it in-place with O(1) extra space?'''


#brute force:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1]
            for i in range(n - 1, 0 ,-1):
                nums[i] = nums[i - 1]
            nums[0] = tmp
            k -= 1
#time complexity: O(n*k)
#space O(1)


#one liner:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
#time c: O(n)
#space c: O(1)

#using reverse:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        def reverse(l:int, r:int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

#time com: O(n)
#space c: O(1)

