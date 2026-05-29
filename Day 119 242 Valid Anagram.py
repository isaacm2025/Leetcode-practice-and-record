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

#hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {} #create a hashmap to store the count of each character in string s
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #for each character in string s, we increment its count in the hashmap, if the character is not already in the hashmap, we initialize its count to 0 and then add 1
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #compare the two hashmaps, if they are the same, then the two strings are anagrams
#time complexity: O(n + m) because we are iterating through both strings once
#space complexity: O(1) because we are only storing the count of each character, and there are only 26 lowercase English letters, so the space used by the hashmaps is constant, 
#O(n + m) if we consider the space used by the hashmaps in the worst case where all characters are unique

