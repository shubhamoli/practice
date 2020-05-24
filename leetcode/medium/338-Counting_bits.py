"""
    Leetcode #338
"""


from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        res[0] = 0

        for i in range(1, num+1):
            res[i] = res[i >> 1] + (i & 1)
        return res

if __name__ == "__main__":

    solution = Solution()

    assert solution.countBits(2) == [0, 1, 1]
    assert solution.countBits(5) == [0,1,1,2,1,2]
