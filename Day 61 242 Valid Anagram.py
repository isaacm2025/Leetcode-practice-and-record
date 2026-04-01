'''Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.'''

#sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
#time complexity: O(n log n + m log m) where n and m are the lengths of s and t respectively
#space complexity: O(n + m) or O(1) if we consider the space used by the sorting algorithm as negligible

#Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #if the lengths of the strings are different, they cannot be anagrams
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1 #count the frequency of each character in s and store it in count_s
            count_t[t[i]] = count_t.get(t[i], 0) + 1 #count the frequency of each character in t and store it in count_t
        return count_s == count_t #if the frequency counts are the same, then s and t are anagrams
#time complexity: O(n + m) where n and m are the lengths of s and t respectively
#space complexity: O(n + m) in the worst case when all characters are unique in both strings, 
#otherwise O(1) if we consider the number of unique characters as a constant (since there are only 26 lowercase English letters)

#hash table with array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 #increment the count for the character in s
            count[ord(t[i]) - ord('a')] -= 1 #decrement the count for the character in t
        for val in count:
            if val != 0: #if any count is not zero, then s and t are not anagrams
                return False
        return True
#time complexity: O(n + m) where n and m are the lengths of s and t respectively
#space complexity: O(1) since the count array has a fixed size of 26 regardless of the input size