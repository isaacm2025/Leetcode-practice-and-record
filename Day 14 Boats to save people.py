'''You are given an integer array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [5,1,4,2], limit = 6

Output: 2
Explanation:
First boat [5,1].
Second boat [4,2].

Example 2:

Input: people = [1,3,2,3,2], limit = 3

Output: 4
Explanation:
First boat [3].
Second boat [3].
Third boat [1,2].
Fourth boat [2].

Constraints:

1 <= people.length <= 50,000
1 <= people[i] <= limit <= 30,000'''

#sorting + two pointers
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
#time complex: O(nlogn)
#space: O(1) or O(n)

#counting sort:
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max[people]
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
                people[idx] = 1
                count[i] -= 1
                idx += 1
        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res
    #time com:O(n)
    #space com: O(m)
    