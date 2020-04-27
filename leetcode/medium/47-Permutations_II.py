"""
    Leetcode #47
"""


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        def helper(curr, used):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]): continue

                curr.append(nums[i])
                used[i] = True
                helper(curr, used)
                used[i] = False
                curr.pop()



        nums.sort()

        # to lock indexes
        used = [False]*len(nums)

        helper([], used)

        return res



if __name__ == "__main__":

    solution = Solution()

    print(solution.permuteUnique([1, 1, 2]))
