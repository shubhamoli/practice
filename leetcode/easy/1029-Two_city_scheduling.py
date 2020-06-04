"""
    Leetcode #1039
"""


from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        tmp = sorted(costs, key=lambda x: x[0] - x[1])

        N = len(tmp)
        total = 0

        for i in range(N):
            if i < N//2:
                total += tmp[i][0]
            else:
                total += tmp[i][1]

        return total


if __name__ == "__main__":

    solution = Solution()

    assert solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110
    assert solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859
