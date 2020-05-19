"""
    Leetcode #228
"""


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []

        tmp = []
        tmp.append(nums[0])
        continuous = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                continuous += 1
            else:
                if continuous > 0:
                    tmp.append("->")
                    tmp.append(nums[i-1])
                res.append("".join(map(str, tmp)))
                # reset tmp and count
                tmp = []
                continuous = 0
                tmp.append(nums[i])

        if tmp:
            if continuous > 0:
                tmp.append("->")
                tmp.append(nums[len(nums)-1])
            res.append("".join(map(str, tmp)))

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert solution.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]


