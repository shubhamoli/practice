"""
    Leetcode #1452
"""


from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        if not favoriteCompanies or not favoriteCompanies[0]:
            return []

        store = {i: set(v) for i, v in enumerate(favoriteCompanies)}
        N = len(favoriteCompanies)

        res = []

        for i in range(N):
            subSet = True
            for j in range(N):
                if i == j: continue     # don't compare same lists
                if not store[i] - store[j]:
                    subSet = False
                    break

            if subSet: res.append(i)

        return res



if __name__ == "__main__":

    solution = Solution()

    assert solution.peopleIndexes([ ["leetcode","google","facebook"],
                                    ["google","microsoft"],
                                    ["google","facebook"],
                                    ["google"],
                                    ["amazon"]]) == [0, 1, 4]

    assert solution.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]) == [0, 1, 2, 3]
