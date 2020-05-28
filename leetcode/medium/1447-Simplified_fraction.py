"""
    Leetcode #1447
"""


from typing import List
import math


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []

        def gcd(i, j):
            while j:
                i, j = j, i % j

            return i

        for i in range(2, n+1):
            for j in range(1, i):
                # if math.gcd(i, j) == 1:
                if gcd(i, j) == 1:
                    res.append("{}/{}".format(str(j), str(i)))

        return res


if __name__ == "__main__":

    solution = Solution()

    print(solution.simplifiedFractions(4)) # ["1/2","1/3","1/4","2/3","3/4"]
