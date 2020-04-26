"""
    Leetcode #40
"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def helper(curr, idx, target):
            if target == 0:
                res.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                # This is needed to avoid dupes
                if i > idx and  candidates[i] == candidates[i-1]:
                    continue

                if target >= candidates[i]:
                    curr.append(candidates[i])
                    helper(curr, i+1, target - candidates[i])
                    curr.pop()

        candidates.sort()
        # 1, 2, 2, 2, 5
        helper([], 0, target)

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.combinationSum2([10,1,2,7,6,1,5], 8))
    print(solution.combinationSum2([2,5,2,1,2], 5))
