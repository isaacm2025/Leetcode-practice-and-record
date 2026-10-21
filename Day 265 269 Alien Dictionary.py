'''There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.

Example 1:

Input: words = ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".


Example 2:

Input: words = ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn" we know 'e' < 'r'
so one possible solution is "hernf"

Example 3:

Input: words = ["abc","ab"]

Output: ""
Explanation:
The second word is a prefix of the first word, but the first word appears before the second. This is impossible in a valid lexicographical ordering, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''

#dfs
from collections import defaultdict
from typing import List
class Solution:
    def alien(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
#time complexity: O(n * m) where n is the number of words and m is the average length of the words. We iterate through each pair of adjacent words to build the graph, which takes O(n * m) time. The DFS traversal also takes O(n * m) time in the worst case.
#space complexity: O(n * m) for the adjacency list and visit dictionary, where n is the number of unique characters in the words and m is the average length of the words. The result list also takes O(n) space, where n is the number of unique characters. Therefore, the overall space complexity is O(n * m).