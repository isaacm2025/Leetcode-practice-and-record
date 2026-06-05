'''You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in 
O
(
l
o
g
(
m
+
n
)
)
O(log(m+n)) time.

Example 1:

Input: nums1 = [1,2], nums2 = [3]

Output: 2.0
Explanation: Among [1, 2, 3] the median is 2.

Example 2:

Input: nums1 = [1,3], nums2 = [2,4]

Output: 2.5
Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
-10^6 <= nums1[i], nums2[i] <= 10^6'''

#bf
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        merged = nums1 + nums2
        merged.sort()
        totalLength = len(merged)
        if totalLength % 2 == 0:
            return (merged[totalLength // 2 - 1] + merged[totalLength // 2]) / 2.0
        else:
            return merged[totalLength // 2]
#time O((m + n) log (m + n)) because we are merging the two arrays and sorting them
#space O(m + n) because we are creating a new array to store the merged elements

#bs optimal
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
#time O(log (min(m, n))) because we are performing binary search on the smaller array
#space O(1) because we are not using any extra space
            