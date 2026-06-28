'''Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.'''

#sorting
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 # count the frequency of each number in nums, if the number is not in the dictionary, get() will return 0 and we add 1 to it
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num]) # create a list of lists where each inner list contains the frequency and the number, so that we can sort the list by frequency
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) # append the number with the highest frequency to the result list, we pop the last element of the sorted list which has the highest frequency
        return res
#time complexity: O(nlogn) where n is the number of distinct elements in nums
#space complexity: O(n) because we are storing the frequency of each number in a dictionary