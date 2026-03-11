'''Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10,000 calls will be made to addWord and search.'''

#brute force
class WordDictionary:

    def __init__(self):
        self.words = set()
        

    def addWord(self, word: str) -> None:
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        for w in self.words:
            if len(w) != len(word):
                continue
            match = True
            for i in range(len(w)):
                if word[i] != '.' and word[i] != w[i]:
                    match = False
                    break
            if match:
                return True
        return False
    
#time complexity: O(n*m) where n is the number of words in the data structure and m is the length of the word being searched.
#space complexity: O(n*m) where n is the number of words in the data structure and m is the average length of the words.