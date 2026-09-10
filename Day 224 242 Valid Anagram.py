'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

Example 3:

Input: s = "x", t = "x"

Output: true

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.'''

#sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
#time complexity: O(nlogn + mlogm)
#space complexity: O(n + m)