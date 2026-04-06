'''You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
Constraints:

1 <= piles.length <= 1,000
piles.length <= h <= 1,000,000
1 <= piles[i] <= 1,000,000,000'''


from typing import List

#brute force
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            if hours <= h:
                return speed
            speed += 1
        return speed
#time complexity: O(n * m) where n is the number of piles and m is the maximum number of bananas in a pile, in the worst case we will have to iterate through all the piles and for each pile we will have to iterate through all the bananas in that pile
#space complexity: O(1) since we are using a constant amount of space to store the speed

#binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r)//2
            totalHours = 0
            for pile in piles:
                totalHours += (pile + mid - 1) // mid
            if totalHours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
#time complexity: O(n * logm) where n is the number of piles and m is the maximum number of bananas in a pile, we are performing a binary search on the speed which takes O(logm) time and for each speed we are iterating through all the piles which takes O(n) time, so the overall time complexity is O(n * logm)
#space complexity: O(1) since we are using a constant amount of space to store the left and right pointers and the mid index