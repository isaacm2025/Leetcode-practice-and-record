'''Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4
Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3

Output: 4
Constraints:

1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000'''

#sorting
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: #sort the array in non-decreasing order, and return the kth largest element in the sorted array, which is the (len(nums) - k)th element in the sorted array
        nums.sort()
        return nums[len(nums) - k] #return the kth largest element in the sorted array, which is the (len(nums) - k)th element in the sorted array

#dont need def __init__ because we are not creating a class, we are just defining a function to solve the problem

#time complexity: O(nlogn) for sorting the array, where n is the number of elements in the array
#space complexity: O(1) for sorting the array in place

#minHeap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1] #use the nlargest function from the heapq module to find the k largest elements in the array, and return the last element in the list of k largest elements, which is the kth largest element in the array
#time complexity: O(nlogk) for finding the k largest elements in the array, where n is the number of elements in the array and k is the number of largest elements to find
#space complexity: O(k) for storing the k largest elements in a list