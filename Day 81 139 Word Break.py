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
s and wordDict[i] consist of only lowercase English letters.'''

#recursion

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict: 
                if ((i + len(word)) <= len(s) and s[i:i + len(word)] == word):
                    if dfs(i + len(word)):
                        return True
            return False
        return dfs(0)
    

#dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if ((i + len(w)) <= len(s) and s[i: i + len(w)] == w):
                    if dfs(i + len(w)):
                        memo[i] = True
            memo[i] = False
            return memo[i]
        return dfs(0)
#time complexity: O(n*m*t) where n is the length of the string, m is the number of words in the dictionary and t is the average length of the words in the dictionary.
#space complexity: O(n) where n is the length of the string.

