'''You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000'''

#brute force:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i: j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False
#time com: O(n^3 log n)
#space com: O(n)

#