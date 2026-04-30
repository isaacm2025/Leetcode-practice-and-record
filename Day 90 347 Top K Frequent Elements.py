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
1 <= k <= number of distinct elements in nums.
'''

#sorting
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
#time complexity: O(n log n) where n is the number of elements in nums. This is because we sort the array of counts which takes O(n log n) time.
#space complexity: O(n) where n is the number of elements in nums. This is because we store the count of each element in a dictionary which takes O(n) space in the worst case when all elements are distinct.

#bucket sort
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
#time complexity: O(n) where n is the number of elements in nums. This is because we count the frequency of each element which takes O(n) time and we also iterate through the frequency array which takes O(n) time in the worst case when all elements are distinct.
#space complexity: O(n) where n is the number of elements in nums. This is because we store the count of each element in a dictionary which takes O(n) space in the worst case when all elements are distinct. Additionally, we also store the frequency of each element in a list which takes O(n) space in the worst case when all elements are distinct.
