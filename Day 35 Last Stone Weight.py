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

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop() #get the two heaviest stones and smash them together
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0
#time complexity: O(n^2 log n) where n is the number of stones
#space complexity: O(1)

#Heap
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoness = [-s for s in stones] #convert to a max heap by negating the values
        heapq.heapify(stoness)
        while len(stoness) > 1:
            first = heapq.heappop(stoness) #get the two heaviest stones and smash them together
            second = heapq.heappop(stoness)
            if second > first:
                heapq.heappush(stoness, first - second)
        stone.append(0) #if there are no stones left, return 0
        return abs(stoness[0]) #return the weight of the last remaining stone
#time complexity: O(n log n) where n is the number of stones
#space complexity: O(n) where n is the number of stones