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
