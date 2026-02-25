'''You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in 
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

from typing import List

#brute force
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums2 + nums1
        merged.sort()

        total_len = len1 + len2
        if total_len % 2 == 0:
            return (merged[total_len // 2 - 1] + merged[total_len // 2]) / 2
        else:
            return merged[total_len // 2]

#time complexity O((n+m)log(n+m))
#space complexity O(n+m) for the merged array

#two pointer approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1): #we only need to iterate until the middle of the merged array
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
        if (len1 + len2) % 2 == 1: #if the total length is odd, we return the middle element which is median1
            return float(median1)
        else:
            return (median1 + median2) / 2.0
        
#time complexity O(n+m) where n and m are the lengths of the two arrays
#space complexity O(1) since we are not using any extra space except for a few variables to keep track of the medians and pointers

#binary search (optimal solution)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2) #we need to find the total length of the merged array to determine the position of the median
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity") #we need to check if the index is out of bounds, if it is we can set it to infinity or negative infinity depending on whether we are looking at the left or right side of the partition
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") #we need to check if the index is out of bounds, if it is we can set it to infinity or negative infinity depending on whether we are looking at the left or right side of the partition
            Bleft = B[j] if j >= 0 else float("-infinity") #we need to check if the index is out of bounds, if it is we can set it to infinity or negative infinity depending on whether we are looking at the left or right side of the partition
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") #we need to check if the index is out of bounds, if it is we can set it to infinity or negative infinity depending on whether we are looking at the left or right side of the partition

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright: #if the left side of the partition is less than or equal to the right side of the partition, then we have found the correct partition
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 #if the total length is even, we need to return the average of the two middle elements which are the maximum of the left side of the partition and the minimum of the right side of the partition
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1 
#time complexity O(log(min(n, m))) where n and m are the lengths of the two arrays
#space complexity O(1) since we are not using any extra space except for a few variables to keep track of the medians and pointers