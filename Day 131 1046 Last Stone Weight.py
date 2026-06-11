'''You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]

Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]

Output: 1
Constraints:

1 <= stones.length <= 20
1 <= stones[i] <= 100'''

#sorting
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
#time complexity: O(n^2 * logn) for sorting the array, where n is the number of stones
#space complexity: O(1) for sorting the array in place

#bs
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort() #sort the array in non-decreasing order
        n = len(stones) 
        while n > 1:
            cur = stones.pop() - stones.pop() #pop the two heaviest stones and calculate the new weight of the stone after smashing them together
            n -= 2
            if cur > 0:
                left, right = 0, n
                while left < right:
                    mid = (left + right) // 2 #use binary search to find the correct position to insert the new stone in the sorted array
                    if stones[mid] < cur: #if the middle element is less than the new stone, we need to search in the right half of the array
                        left = mid + 1
                    else:
                        right = mid
                pos = left
                n += 1
                stones.append(0)
                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = cur
        return stones[0] if stones else 0
#time complexity: O(n^2) for popping the two heaviest stones and inserting the new stone in the correct position, where n is the number of stones
#space complexity: O(1) for sorting the array in place and inserting the new stone in the correct position

#heap
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] #convert the weights to negative values to use a min heap as a max heap
        heapq.heapify(stones) #heapify the array to create a min heap
        while len(stones) > 1:
            first = heapq.heappop(stones) #pop the two heaviest stones from the min heap
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second) #if the second stone is heavier than the first stone, we need to push the new stone with weight (second - first) back into the min heap
        stones.append(0) #if there are no stones left, we need to return 0
        return abs(stones[0]) #return the weight of the last remaining stone, which is the absolute value of the only element left in the min heap
#time complexity: O(nlogn) for heapifying the array and popping the two heaviest stones, where n is the number of stones
#space complexity: O(n) for storing the stones in the min heap