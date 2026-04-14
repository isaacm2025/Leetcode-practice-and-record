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
1 <= target <= 30
'''

from typing import List
#bf
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            generate_subsets(i + 1, cur, total + candidates[i])
            cur.pop()
            generate_subsets(i + 1, cur, total)
        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]
    
#backtracking (optimized)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[list[int]]:
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
#time complexity: O(n * 2^n) where n is the number of candidates. In the worst case, we may have to explore all possible combinations of candidates, which can be up to 2^n. Additionally, we need to copy the current path to the result list, which takes O(n) time. Therefore, the overall time complexity is O(n * 2^n).
#space complexity: O(n) for the recursion stack and the path list. In the worst case, the depth of the recursion can be up to n, and the path list can also contain up to n elements. Therefore, the overall space complexity is O(n).