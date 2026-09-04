'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
Constraints:

1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
'''

#recursion
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True
            for w in wordDict:
                if ((i + len(w)) <= len(s) and s[i:i + len(w)] == w):
                    if dfs(i + len(w)):
                        return True
            return False
        return dfs(0)
#time complexity: O(t * m^n) where t is the number of words in the dictionary, m is the average length of the words, and n is the length of the string s. This is because for each character in s, we may check all words in wordDict.
#space complexity: O(n) where n is the length of the string s. This is because we are using a recursive function that can go as deep as the length of s in the worst case.

#hashset
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        def dfs(i):
            if i == len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False
        return dfs(0)
#time complexity: O((n * 2^n) + m) where n is the length of the string s and m is the number of words in the dictionary. This is because for each character in s, we may check all possible substrings and for each substring, we may check if it is in the wordSet.
#space complexity: O(n + (mt)), where n is the length of the string s, m is the number of words in the dictionary, and t is the average length of the words. This is because we are using a recursive function that can go as deep as the length of s in the worst case and we are also storing the words in a set.

#dp
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
#time complexity: O(n * m * k) where n is the length of the string s, m is the number of words in the dictionary, and k is the average length of the words. This is because for each character in s, we may check all words in wordDict and for each word, we may check if it matches the substring of s.
#space complexity: O(n) where n is the length of the string s. This is because we are using a dp array of size n + 1 to store the results of subproblems.