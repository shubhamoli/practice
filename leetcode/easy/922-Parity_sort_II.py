"""
    Leetcode #922
"""


from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        res = [-1] * len(A)
        for i in range(len(A)):
            if i % 2 == 0:
                res[i] = even.pop()
            else:
                res[i] = odd.pop()

        return res

    def sortArrayByParityII_OPTI(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1

        res = [-1] * len(A)
        for i in A:
            if i % 2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res




if __name__ == "__main__":

    solution = Solution()

    print(solution.sortArrayByParityII([4,2,5,7]))  # [4,7,2,5], [2,5,4,7], [2,7,4,5]
    print(solution.sortArrayByParityII_OPTI([4,2,5,7]))  # [4,7,2,5], [2,5,4,7], [2,7,4,5]

