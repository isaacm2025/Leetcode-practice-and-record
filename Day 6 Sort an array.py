'''You are given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [10,9,1,1,1,2,3,1]

Output: [1,1,1,1,2,3,9,10]
Example 2:

Input: nums = [5,10,2,1,3]

Output: [1,2,3,5,10]
Constraints:

1 <= nums.length <= 50,000.
-50,000 <= nums[i] <= 50,000'''

#quick sort
from collections import defaultdict
from typing import List


class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[left]

        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] > nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] > nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]
        
        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] < pivot:
                    break
            while True:
                j -= 1
                if not nums[j] > pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j
    
    def quick_sort(self, nums: List[int], left: int, right: int) -> None:
        if right <= left + 1:
            if right == left + 1 and nums[right] < nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            return
        
        j = self.partition(nums, left, right)
        self.quick_sort(nums, left, j - 1)
        self.quick_sort(nums, j + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
    
    #time complexity: O(nlog(n)) in average case, O(n^2) in worst case
    #space complexity: O(log(n)) due to recursion stack


#merge sort approach
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def merge_sort(arr, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)

        merge_sort(nums, 0, len(nums) - 1)
        return nums
    
    #time complexity: O(nlog(n))
    #space complexity: O(n) due to temporary arrays used in merging


    #Heap sort approach can also be used to solve this problem with O(1) space complexity.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapSort(nums)
        return nums
    def heapify(self, arr, n, i):
        l = (i << 1) + 1
        r = (i << 1) + 2
        largestNode = i

        if l < n and arr[l] > arr[largestNode]:
            largestNode = l
        if r < n and arr[r] > arr[largestNode]:
            largestNode = r
        if largestNode != i:
            arr[i], arr[largestNode] = arr[largestNode], arr[i]
            self.heapify(arr, n, largestNode)

    def heapSort(self, arr):
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

    #time complexity: O(nlog(n))
    #space complexity: O(log n) due to recursion stack in heapify function

    #continue sorting
    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            def counting_sort():
                count = defaultdict(int)
                minVal, maxVal = min(nums), max(nums)
                for val in nums:
                    count[val] += 1

                index = 0
                for val in range(minVal, maxVal + 1):
                    while count[val] > 0:
                        nums[index] = val
                        index += 1
                        count[val] -= 1

            counting_sort()
            return nums
        
    #time complexity: O(n + k) where k is the range of the input values
    #space complexity: O(n)

    #shell sort approach
    class Solution:
        def sortArray(self, nums: List[int]) -> List[int]:
            def shell_sort(nums, n):
                gap = n // 2
                while gap >= 1:
                    for i in range(gap,n):
                        temp = nums[i]
                        j = i - gap
                        while j >= 0 and nums[j] > temp:
                            nums[j + gap] = nums[j]
                            j -= gap
                        nums[j + gap] = temp
                    gap //= 2
            n = len(nums)
            if n == 1:
                return nums
            shell_sort(nums, n)
            return nums
    #time complexity: O(n log n) in average case
    #space complexity: O(1)

    
        

            