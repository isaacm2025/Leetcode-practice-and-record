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
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create dictionary to count the frequency of each element in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1 #update the count of num in the dictionary, if num is not in the dictionary, get() will return 0 and we add 1 to it
        arr = [] #create a list to store the key-value pairs of the count dictionary, where key is the element and value is its frequency
        for key, value in count.items(): 
            arr.append([key, value]) #append the key-value pairs to the arr list
        arr.sort() #sort the arr list based on the frequency of the elements, which is the second element of the key-value pair
        res = [] #create a list to store the k most frequent elements
        while len(res) < k: #while the length of the res list is less than k, we pop the last element from the arr list, which is the key-value pair with the highest frequency, and append the key (the element) to the res list
            res.append(arr.pop()[1]) #append the key (the element) to the res list, which is the second element of the key-value pair
        return res
#time complexity: O(nlogn)
#space complexity: O(n) because of the count dictionary and arr list

#bucket sort
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create dictionary to count the frequency of each element in nums
        freq = [[] for i in range(len(nums) + 1)] #create a list of empty lists, where the index of the outer list represents the frequency of the elements, and the inner lists will store the elements with that frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1 #update the count of num in the dictionary, if num is not in the dictionary, get() will return 0 and we add 1 to it
        for key, value in count.items(): #iterate through the key-value pairs of the count dictionary, where key is the element and value is its frequency, and append the key (the element) to the inner list of the freq list at the index of its frequency
            freq[value].append(key)
        res = []
        for i in range(len(freq) -1, 0, -1): #iterate through the freq list in reverse order, starting from the last index (the highest frequency) to the first index (the lowest frequency), and append the elements in the inner lists to the res list until we have k elements in the res list
            for num in freq[i]:
                res.append(num) #append the elements in the inner list to the res list
                if len(res) == k:
                    return res
#time complexity: O(n)
#space complexity: O(n) because of the count dictionary and freq list