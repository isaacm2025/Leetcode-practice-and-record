'''Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 100,000
1 <= t.length <= 100,000
s and t consist of uppercase and lowercase English letters.'''

#bf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res, resLen = [-1, -1], float("inf")
        for i in range(len(s)):
            countS = {}
            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)
                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                if flag and j - i + 1 < resLen:
                    res = [i, j]
                    resLen = j - i + 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""
#time complexity: O(n^2)
#space complexity: O(n)
