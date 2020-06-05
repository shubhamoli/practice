"""
    Leetcode #698
"""


from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        _sum = sum(nums)
        if _sum % k:
            return False

        target = _sum // k
        seen = [0] * len(nums)

        # speeds things up, as larger numbers are tried first if its not possible
        # to get k subsets we will know sooner
        nums.sort(reverse=True)

        def helper(k, idx, curr_sum):
            if k == 1:
                return True

            if curr_sum == target:
                return helper(k-1, 0, 0)

            for i in range(idx, len(nums)):
                if not seen[i] and curr_sum + nums[i] <= target:
                    seen[i] = 1
                    if helper(k, i+1, curr_sum + nums[i]):
                        return True
                    seen[i] = 0

            return False

        return helper(k, 0, 0)


if __name__ == "__main__":

    solution = Solution()

    assert solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) == True
    assert solution.canPartitionKSubsets([2,2,2,2,3,4,5], 4) == False
