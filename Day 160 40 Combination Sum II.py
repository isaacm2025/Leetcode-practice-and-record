'''You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]
Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30'''

#backtracking
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()
        dfs(0, [], 0)
        return res
#time complexity: O(n * 2^n) where n is the length of the input array. In the worst case, we can have a combination of size n, and for each element, we have two choices: include it or not. Therefore, the total number of combinations is 2^n. For each valid combination, we may take O(n) time to copy it to the result list.
#space complexity: O(n) for the recursion stack and the path list, where n is the length of the input array. The maximum depth of the recursion tree is n, and the path list can also have a maximum size of n. The result list will take O(k) space to store all combinations, where k is the number of valid combinations.