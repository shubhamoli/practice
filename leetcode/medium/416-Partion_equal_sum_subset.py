"""
    Leetcode #416
"""


from typing import List

class Solution:
    def canPartition(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        memo = {}
        def helper(idx, target):
            if target < 0:
                return False

            if target == 0:
                return True

            if memo.get((idx, target)) is not None:
                return memo.get((idx, target))

            for i in range(idx, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True

            memo[(idx, target)] = False
            return False

        _sum = sum(nums)
        nums.sort(reverse=True)
        return False if _sum % 2 else helper(0, _sum // 2)  # since odd sum can't be divided in 2 equal parts


if __name__ == "__main__":

    solution = Solution()

    assert solution.canPartition([1, 5, 11, 5], 2) == True
    assert solution.canPartition([1, 2, 3, 5], 2) == False

