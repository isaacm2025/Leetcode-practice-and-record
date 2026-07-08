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
            current = stones.pop() - stones.pop() # because we are popping the last two elements, we are guaranteed to have the two largest stones. This will equal to zero if the two stones are equal, or the difference between the two stones if they are not equal.
            if current > 0:
                stones.append(current)
        return stones[0] if stones else 0
#time complexity: O(n^2 * logn) for sorting the array each time we smash two stones
#space complexity: O(n) for storing the stones in the array.

#bs
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)
        while len(stones) > 1:
            current = stones.pop() - stones.pop()
            n -= 2
            if current > 0:
                left, right = 0, n
                while left < right:
                    mid = (left + right) // 2
                    if stones[mid] < current:
                        left = mid + 1
                    else:
                        right= mid
                pos = left
                n += 1
                stones.append(0)
                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = current
        return stones[0] if n > 0 else 0
#time complexity: O(n^2) for inserting the new stone into the sorted array each time we smash two stones
#space complexity: O(1) or O(n) depending on the implementation of the list in Python.