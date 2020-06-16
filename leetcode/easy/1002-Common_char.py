"""
    Leetcode #1002
"""


from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []

        res = list(A[0])

        for word in A[1:]:
            _tmp = []
            for c in word:
                # check char present in prev word
                # if presend remove from prev and add in current
                if c in res:
                    _tmp.append(c)
                    res.remove(c)

            # replace prev with current set of common char
            res = _tmp

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.commonChars(["bella","label","roller"]) == ["l", "l", "e"]
    assert solution.commonChars(["cool","lock","cook"]) == ["c", "o"]

