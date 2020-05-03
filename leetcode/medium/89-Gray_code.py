"""
    Leetcode #89
"""


from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        res = []

        total = 2 **n

        for i in range(total):
            res.append(i ^ (i >> 1))

        return res


if __name__ == "__main__":

    print(Solution().grayCode(2))   # [0, 1, 3, 2]
    print(Solution().grayCode(0))
