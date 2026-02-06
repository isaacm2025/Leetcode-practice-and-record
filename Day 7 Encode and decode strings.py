'''Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: # edge case
            return "" # edge case
        sizes, res = [], "" # sizes to store lengths of strings
        for s in strs: # iterate through strings
            sizes.append(len(s)) # append lengths to sizes
        for sz in sizes: # iterate through sizes
            res += str(sz) # append size to result
            res += ',' # delimiter
        res += '#' # delimiter between sizes and strings
        for s in strs: # iterate through strings
            res += s # append strings to result
        return res # return result

    def decode(self, s: str) -> List[str]:
        if not s:# edge case
            return [] # edge case
        sizes, res, i = [], [], 0 # sizes to store lengths of strings, res to store result strings, i as index
        while s[i] != '#': # iterate until delimiter
            cur = "" # current size string
            while s[i] != ',': # iterate until delimiter
                cur += s[i] # append character to current size
                i += 1 # increment index
            sizes.append(int(cur)) # append size to sizes
            i += 1 # skip delimiter
        i += 1 # skip '#'
        for sz in sizes: # iterate through sizes
            res.append(s[i:i+sz]) # append substring of size sz to result
            i += sz # increment index by size
        return res # return result
#time complexity: O(N) for each encode and decode
#space complexity: O(M+N) for each encode and decode where M is number of strings and N is total length of all strings

#optimal soltion
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
#time complexity: O(N) for each encode and decode
#space complexity: O(M+N) for each encode and decode where M is number of



