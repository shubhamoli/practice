"""
    Leetcode #376
"""


from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxLen = 1
        p = 0   # positive sum
        n = 0   # negative sum

        if nums[1] - nums[0] > 0:
            p += 1
            maxLen += 1
        elif nums[1] - nums[0] < 0:
            n += 1
            maxLen += 1

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] > 0 and (p == 0 or p == -1):
                p += 1
                n -= 1
                maxLen += 1
            elif nums[i] - nums[i-1] < 0 and (n == 0 or n == -1):
                n += 1
                p -= 1
                maxLen += 1
            else:
                pass

        return maxLen


if __name__ == "__main__":

    assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
