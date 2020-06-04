"""
    Leetcode #679
"""


from typing import List

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return round(nums[0], 4) == 24

        N = len(nums)

        for i in range(N-1):
            for j in range(i+1, N):
                # skipping nums[i] and nums[j]
                remain = nums[:i] + nums[i+1:j] + nums[j+1:]

                l, r = nums[i], nums[j]

                if self.judgePoint24(remain + [l + r]):
                    return True

                if self.judgePoint24(remain + [l - r]) or self.judgePoint24(remain + [r - l]):
                    return True

                if self.judgePoint24(remain + [l * r]):
                    return True

                if (r and self.judgePoint24(remain + [l / r])) or (l and self.judgePoint24(remain + [r / l])):
                    return True

        return False


if __name__ == "__main__":

    solution = Solution()

    assert solution.judgePoint24([4, 1, 8, 7]) == True
    assert solution.judgePoint24([1, 2, 1, 2] ) == False

