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


from typing import List
from collections import Counter
#sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1 #count the frequency of each number in nums and store it in count
        arr = []
        for num, freq in count.items():
            arr.append((freq, num)) #create a list of tuples (frequency, number) for sorting
        arr.sort(reverse=True) #sort the list of tuples in descending order based on frequency
        res = []
        for i in range(k):
            res.append(arr[i][1]) #append the number corresponding to the top k frequencies to the result list
        return res
#time complexity: O(n log n) due to sorting the list of tuples
#space complexity: O(n) for the count dictionary and the list of tuples
