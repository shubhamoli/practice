"""
    Leetcode #39
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(idx, target, curr):
            if target == 0:
                result.append(curr[:])
                return

            for i in range(idx, len(candidates)):
                if target >= candidates[i]:
                    curr.append(candidates[i])
                    helper(i, target - candidates[i], curr)
                    curr.pop()

        helper(0, target, [])
        return result


if __name__ == "__main__":

    solution = Solution()

    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([2, 3, 5], 8))

