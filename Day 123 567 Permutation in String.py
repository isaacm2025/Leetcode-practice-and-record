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

#bf
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i:j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False
#time: O(n^3 log n) because of the nested loop and sorting the substring in each iteration
#space: O(n) because of the sorted list

#hashtable
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
#time: O(n * m) because of the nested loop
#space: O(1) at most 26 characters in the hashtable
