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

#topological sort
from typing import List
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        q = deque([c for c in set("".join(words)) if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(res) if len(res) == len(set("".join(words))) else ""
#time complexity: O(n * m) where n is the number of words and m is the average length of the words
#space complexity: O(V + E) where V is the number of unique characters and E is the number of edges in the graph