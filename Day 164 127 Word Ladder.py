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
1 <= wordList.length <= 100'''

#bfs
from collections import deque
class Solution:
    def wordLadder(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        words, res = set(wordList), 0
        queue = deque([beginWord])
        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in range(97, 123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node[i + 1:]
                        if nei in words:
                            queue.append(nei)
                            words.remove(nei)
        return 0
#time complexity: O(m^2 * n) where m is the length of each word and n is the number of words in the wordList. For each word, we generate all possible one-letter transformations (m * 25) and check if they are in the wordList (O(1) for set lookup).
#space complexity: O(m^2 * n) where m is the length of each word and n is the number of words in the wordList. We store all the words in a set for O(1) lookups, which takes O(m * n) space. The queue can hold at most O(n) words, and each word can have at most O(m^2) transformations, leading to a total space complexity of O(m^2 * n).
