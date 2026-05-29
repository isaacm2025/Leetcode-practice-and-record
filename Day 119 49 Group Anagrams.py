'''Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''

#sorting
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #we use a defaultdict to store the anagrams, the key will be the sorted version of the string and the value will be a list of strings that are anagrams of each other
        for s in strs:
            sortedS = ''.join(sorted(s)) #we sort the string and join it back to a string, this will be the key in our hashmap, all anagrams will have the same sorted version, so they will be grouped together in the same list
            res[sortedS].append(s) #we append the original string to the list of anagrams corresponding to the sorted version of the string
        return list(res.values()) #we return the values of the hashmap as a list, each value is a list of anagrams
    
#time complexity: O(n * k log k) where n is the number of strings in the input list and k is the maximum length of a string in the input list, because we are sorting each string which takes O(k log k) time and we are doing this for n strings
#space complexity: O(n * k) because in the worst case, all strings are anagrams of each other and we have to store all n strings in the output list, and each string can have a maximum length of k, so the space used by the output list is O(n * k)

#hash table
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #we use a defaultdict to store the anagrams, the key will be a tuple representing the count of each character in the string and the value will be a list of strings that are anagrams of each other
        for s in strs:
            count = [0] * 26 #we create a list of size 26 to count the frequency of each character in the string, we initialize it with 0, and we will increment the count for each character in the string
            for c in s:
                count[ord(c) - ord('a')] += 1 #we increment the count for the character c, we use ord to get the ASCII value of the character and we subtract the ASCII value of 'a' to get the index in the count list corresponding to the character, for example, if c is 'a', then ord(c) - ord('a') will be 0, if c is 'b', then ord(c) - ord('a') will be 1, and so on
            res[tuple(count)].append(s) #we convert the count list to a tuple so that it can be used as a key in the hashmap, all anagrams will have the same count of characters, so they will be grouped together in the same list
        return list(res.values()) #we return the values of the hashmap as a list, each value is a list of anagrams
    
#time complexity: O(n * k) where n is the number of strings in the input list and k is the maximum length of a string in the input list, because we are counting the frequency of each character in each string which takes O(k) time and we are doing this for n strings
#space complexity: O(n * k) because in the worst case, all strings are anagrams of each other and we have to store all n strings in the output list, and each string can have a maximum length of k, so the space used by the output list is O(n * k)