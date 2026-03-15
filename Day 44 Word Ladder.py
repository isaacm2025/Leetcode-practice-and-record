'''You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

Your goal is to transform beginWord into endWord by following the rules:

You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]

Output: 4
Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".

Example 2:

Input: beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sat","dag","dot"]

Output: 0
Explanation: There is no possible transformation sequence from "cat" to "sag" since the word "sag" is not in the wordList.

Constraints:

1 <= beginWord.length <= 10
1 <= wordList.length <= 100
'''

from collections import deque
from typing import List
#BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, res = set(wordList), 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in (97, 123):
                        if chr(c) == node[i]:
                            continue
                        neighbor = node[:i] + chr(c) + node[i + 1:]
                        if neighbor in words:
                            q.append(neighbor)
                            words.remove(neighbor)
        return 0
#time complexity: O(m^2 * n) where m is the length of wordList and n is the length of each word in wordList. 
#We iterate through each word in wordList and for each word, we iterate through each character to find its neighbors. 
# Finding neighbors takes O(n) time, and we do this for all m words, resulting in O(m * n) time complexity. Additionally, we perform a BFS which can take O(m) time in the worst case, leading to an overall time complexity of O(m^2 * n).
#space complexity: O(m^2 * n) due to the space used for the queue and the set of words. In the worst case, we may have to store all words in the queue and the set, leading to O(m) space complexity. Additionally, we may generate up to O(m * n) neighbors for each word, resulting in O(m^2 * n) space complexity.

#BFS 3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0
#time complexity: O(m^2 * n) where m is the length of wordList and n is the length of each word in wordList. 
# We iterate through each word in wordList and for each word, we iterate through each character to create patterns. 
# Creating patterns takes O(n) time, and we do this for all m words, resulting in O(m * n) time complexity. 
# Additionally, we perform a BFS which can take O(m) time in the worst case, leading to an overall time complexity of O(m^2 * n).
#space complexity: O(m^2 * n) due to the space used for the queue, the set of visited words, and the dictionary of neighbors. 
# In the worst case, we may have to store all words in the queue and the set, leading to O(m) space complexity. 
# Additionally, we may generate up to O(m * n) patterns for each word, and each pattern can have up to O(m) neighbors, 
# resulting in O(m^2 * n) space complexity.
