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
            for w in wordDict:
                if ((i + len(w)) <= len(s) and s[i:i + len(w)] == w):
                    if dfs(i + len(w)):
                        return True
            return False
        return dfs(0)
#time O(t * m^n) where t is the number of words in the dictionary, m is the average length of the words, and n is the length of the input string s. 
#This is because in the worst case, we may have to check each word in the dictionary for each character in the input string.
#space O(n) because of the recursive call stack, where n is the length of the input string s.

#hashset
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        def dfs(i):
            if i == len(s):
                return True
            for j in range(i + 1, len(s)):
                if s[i:j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False
        return dfs(0)
#time O(n^2) because of the nested loops, where n is the length of the input string s. 
#space O(n) because of the recursive call stack, where n is the length of the input string s, and O(m) for the hash set where m is the number of words in the dictionary.