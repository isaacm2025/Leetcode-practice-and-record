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
1 <= piles[i] <= 1,000,000,000
'''
from typing import List

#brute force:
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1 #initialize the speed to 1, which is the minimum possible speed
        while True:
            total_hours = 0
            for pile in piles:
                total_hours += (pile + speed - 1) // speed #calculate the number of hours needed to eat the current pile at the current speed
            if total_hours <= h:
                return speed
            speed += 1
#time complexity: O(n*m) where n is the number of piles and m is the maximum number of bananas in a pile
#space complexity: O(1)