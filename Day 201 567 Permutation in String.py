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

1 <= s1.length, s2.length <= 10000'''

#hashtable
class Solution:
    def check(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count2[s2[j]] == count1.get(s2[j], 0):
                    cur += 1
                elif count2[s2[j]] > count1.get(s2[j], 0):
                    break
                if cur == need:
                    return True
        return False
#time complexity: O(n * m) where n is the length of s2 and m is the length of s1
#space complexity: O(1) since the size of the hashtable is limited to 26 lowercase letters