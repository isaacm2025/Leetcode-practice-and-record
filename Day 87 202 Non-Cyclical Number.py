#hash set
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1
#tc: O(log n)
#sc: O(log n)