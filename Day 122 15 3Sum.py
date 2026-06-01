'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5'''

#bf
from ast import List
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
#time O(n^3) because we have three nested loops that iterate through the input array, where n is the length of the input array.
#space O(n) because we are using a set to store the unique triplets that sum up to zero, and in the worst case, we could have n/3 unique triplets, which would require O(n) space to store.

#hashmap
from ast import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort the input array to avoid duplicates and to make it easier to find triplets that sum up to zero
        count = defaultdict(int) #create a dictionary to store the count of each number in the input array
        for num in nums:
            count[num] += 1 #populate the count dictionary with the count of each number in the input array
        res = [] #initialize an empty list to store the resulting triplets that sum up to zero
        for i in range(len(nums)):
            count[nums[i]] -= 1 #decrement the count of the current number in the count dictionary to avoid using the same number multiple times in the triplet
            if i and nums[i] == nums[i - 1]:#if the current number is the same as the previous number, skip it to avoid duplicates in the resulting triplets
                continue
            for j in range(i + 1, len(nums)): #iterate through the remaining numbers in the input array starting from the index after the current number
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]: #if the current number is the same as the previous number, skip it to avoid duplicates in the resulting triplets
                    continue
                target = -nums[i] - nums[j] #calculate the target number that we need to find in the count dictionary to complete the triplet that sums up to zero
                if count[target] > 0:
                    res.append([nums[i], nums[j], target]) #if the target number exists in the count dictionary and its count is greater than zero, it means we have found a triplet that sums up to zero, so we add it to the resulting list of triplets
            for j in range(i + 1, len(nums)): #after we have finished checking for triplets with the current number and the next number, we need to restore the count of the next number in the count dictionary before moving on to the next iteration of the outer loop
                count[nums[j]] += 1
        return res
#time O(n^2) because we have two nested loops that iterate through the input array, where n is the length of the input array. The innermost operation of checking if the target number exists in the count dictionary takes O(1) time on average, so it does not contribute to the overall time complexity.
#space O(n) because we are using a dictionary to store the count of each number in the input array, which in the worst case could require O(n) space if all numbers in the input array are unique. Additionally, we are using a list to store the resulting triplets, which could also require O(n) space in the worst case if there are many triplets that sum up to zero.