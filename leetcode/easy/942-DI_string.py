"""
    Leetcode #942
"""


from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = 0
        r = len(S)

        res = []
        for i in S:
            if i == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1

        return res + [l]


if __name__ == "__main__":

    solution = Solution()

    assert solution.diStringMatch("IDID") == [0,4,1,3,2]
    assert solution.diStringMatch("DDI") == [3,2,0,1]

