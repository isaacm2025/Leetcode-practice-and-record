'''There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100'''

from collections import defaultdict, deque
from typing import List

#DFS
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
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
        visited = {}
        res = []
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            visited[c] = False
            res.append(c)
        for i in adj:
            if dfs(i):
                return ""
        res.reverse()
        return "".join(res)
#time complexity: O(N + V + E) where N is the total number of characters in the input, V is the number of unique characters and E is the number of edges in the graph.
#space complexity: O(V + E) where V is the number of unique characters and E is the number of edges in the graph.
            

#Topological sort
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

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
        queue = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for neighbor in adj[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(res) < len(indegree):
            return ""
        return "".join(res)
#time complexity: O(N + V + E) where N is the total number of characters in the input, V is the number of unique characters and E is the number of edges in the graph.
#space complexity: O(V + E) where V is the number of unique characters and E is the number of edges in the graph.