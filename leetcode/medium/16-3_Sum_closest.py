"""
    Leetcode #16
"""


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0

        # O(nlogn)
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while (l < r):
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                if abs(total - target) < abs(closest - target):
                    closest = total

                # closest = min(closest, target)

                if total > target:
                    r -= 1
                else:
                    l += 1


        return closest



if __name__ == "__main__":

    solution = Solution()

    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
