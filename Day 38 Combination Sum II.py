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

from collections import defaultdict
from typing import List, list

#brute force
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def generate_subsets(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i >= len(candidates):
                return
            cur.append(candidates[i])
            generate_subsets(i + 1, cur, total + candidates[i])
            cur.pop()
            generate_subsets(i + 1, cur, total)
        generate_subsets(0, [], 0)
        return [list(combination) for combination in res]
#time complexity: O(n * 2^n) where n is the length of candidates
#space complexity: O(n *2^n) for the recursion stack and O(k) for the result list

#hashmap
class Solution:
    def combinationSum2(self, nums, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.count = defaultdict(int)
        cur = []
        A = []

        for num in nums:
            if self.count[num] == 0:
                A.append(num)
            self.count[num] += 1
        self.backtrack(A, target, 0, cur)
        return self.res
    def backtrack(self, nums, A, target, i, cur):
        if target == 0:
            self.res.append(cur.copy())
            return
        if target < 0 or i >= len(nums):
            return
        if self.count[nums[i]] > 0:
            cur.append(nums[i])
            self.count[nums[i]] -= 1
            self.backtrack(A, target - nums[i], i, cur)
            cur.pop()
            self.count[nums[i]] += 1
        self.backtrack(nums, target, cur, i + 1)
#time complexity: O(n * 2^n) where n is the length of candidates
#space complexity: O(n *2^n) for the recursion stack and O(k) for the result list

#backtracking optimal
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
#time complexity: O(n * 2^n) where n is the length of candidates
#space complexity: O(n) for the recursion stack and O(k) for the result list