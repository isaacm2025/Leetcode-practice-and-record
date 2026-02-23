'''A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:

Input: weights = [2,4,6,1,3,10], days = 4

Output: 10
Explanation:
1st day: [2]
2nd day: [4,6]
3rd day: [1,3]
4th day: [10]

Example 2:

Input: weights = [1,2,3,4,5], days = 5

Output: 5
Explanation:
1st day: [1]
2nd day: [2]
3rd day: [3]
4th day: [4]
5th day: [5]

Example 3:

Input: weights = [1,5,4,4,2,3], days = 3

Output: 8
Explanation:
1st day = [1,5]
2nd day = [4,4]
3rd day = [2,3]

Constraints:

1 <= days, weights.length <= 50,000
1 <= weights[i] <= 500'''

from typing import List

#linear search:
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = max(weights) #the minimum capacity of the ship must be at least the maximum weight in the weights array, otherwise we cannot ship that package
        while True:
            ships = 1
            cap = res #initialize the capacity of the ship to the current result, which is the minimum capacity we are testing
            for weight in weights:
                if cap < weights:
                    ships += 1 #if the current capacity of the ship is less than the current weight, we need to use another ship
                    cap = res #reset the capacity of the ship to the current result, which is the minimum capacity we are testing
                cap -= weight #subtract the current weight from the capacity of the ship
            
            if ships <= days:
                return res
            
            res += 1
#time complexity: O(n^2) where n is the number of weights
#space complexity: O(1)