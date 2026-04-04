'''You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length'''

#brute force
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(26):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf > k:
                    res = max(res, j - i)
                    count[s[i]] -= 1
                    i += 1
            res = max(res, len(s) - i)
        return res
#time complexity: O(26 * n) where n is the length of the string
#space complexity: O(26) which is the size of the count dictionary
