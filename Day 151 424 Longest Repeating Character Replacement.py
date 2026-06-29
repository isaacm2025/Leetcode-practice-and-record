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
0 <= k <= s.length
'''

#bf
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count, maxf = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
#time complexity: O(n^2), where n is the length of the string. 
# The outer loop iterates through each character in the string, and the inner loop iterates through the remaining characters to calculate the frequency of each character in the substring. In the worst case, this results in a time complexity of O(n^2).
#space complexity: O(1), since the count dictionary can have at most 26 entries (one for each uppercase English letter), which is a constant space usage.

#sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
#time complexity: O(n), where n is the length of the string. 
#Each character is processed at most twice, once when it is added to the count dictionary and once when it is removed.
#space complexity: O(1), since the count dictionary can have at most 26 entries (one for each uppercase English letter), which is a constant space usage.