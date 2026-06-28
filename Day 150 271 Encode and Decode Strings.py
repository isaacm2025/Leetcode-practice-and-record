'''Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]

Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);

Example 2:

Input: strs = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Follow up: Could you write a generalized algorithm to work on any possible set of characters?'''

#optimal
from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)
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
#time complexity: O(m + n) where m is the total length of all strings in the input list and n is the length of the encoded string.
#space complexity: O(m + n) where m is the total length of all strings in the input list and n is the length of the encoded string.