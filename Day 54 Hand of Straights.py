'''You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.

Example 1:

Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4

Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].

Example 2:

Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4

Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.

Constraints:

1 <= hand.length <= 1000
0 <= hand[i] <= 1000
1 <= groupSize <= hand.length'''



from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True
#time complexity: O(nlogn)
#space complexity: O(n)

#Heap
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
#time complexity: O(nlogn)
#space complexity: O(n)

#hashmap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1] > 0:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if count[i] == 0:
                            return False
                        count[i] -= 1
                start += 1
        return True
#time complexity: O(n)
#space complexity: O(n)