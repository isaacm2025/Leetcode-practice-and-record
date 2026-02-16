'''You are given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
Example 1:

Input: arr = [2,4,5,8], k = 2, x = 6

Output: [4,5]
Example 2:

Input: arr = [2,3,4], k = 3, x = 1

Output: [2,3,4]
Constraints:

1 <= k <= arr.length <= 10,000.
-10,000 <= arr[i], x <= 10,000
arr is sorted in ascending order.
'''
from typing import List
#sorting
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key= lambda num: (abs(num - x), num))
        return sorted(arr[:k])
    
#time com: O(n log n + k log k)
#space com: O(1) or O(n) space depending on the sorting, O(k) for the output array.

#two pointers:
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l: r + 1]
#time com: O(n - k)
#space com: O(k)

#binary search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) //2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l: l + k]
#time com: O(log(n-k) + k)
#space com: O(k) for the output array

