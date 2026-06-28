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
            return False
        return sorted(s) == sorted(t) #returns True if the sorted version of both strings are equal, otherwise returns False
#time complexity: O(nlogn + mlogm) because of sorting, n and m are the lengths of the strings, logn and logm because of the sort function, sorting function is O(nlogn) because it uses Timsort algorithm
#space complexity: O(n + m) because we are creating a new sorted version of the strings,

#hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {} # create two dictionaries to store the counts of each character in the strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0) # get the current count of the character in the dictionary, if it doesn't exist, return 0
        return countS == countT # returns True if the two dictionaries are equal, otherwise returns False
#time complexity: O(n + m) because we are going through the entire strings once,
#space complexity: O(1) since we have at mostt 26 characters in the English alphabet, the space used by the dictionaries is constant
