'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.'''


#sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #if the lengths of the two strings are different, then they cannot be anagrams
        return sorted(s) == sorted(t) #sort both strings and compare them, if they are the same, then they are anagrams
#time complexity: O(nlogn + mlogm) because we are sorting both strings
#space complexity: O(n + m) because we are creating new sorted lists for both strings, or O(1) if we consider the space used by the sorting algorithm