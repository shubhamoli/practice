"""
    Leetcode #17
"""

from typing import List

class Solution:

    def letterCombinations_ITER(self, digits: str) -> List[str]:
        if not digits:
            return []

        try:
            tmp = int(digits)
        except Exception as e:
            return []

        res = []
        store = {
                "1": [],
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 1:
            return store[digits]

        res = [""]

        for i in range(len(digits)):
            tmp = []
            a = store[digits[i]]
            for j in range(len(a)):
                for k in range(len(res)):
                    tmp.append(res[k]+a[j])
            res = tmp

        return res

    def letterCombinations_RECUR(self, digits: str) -> List[str]:
        if not digits:
            return []

        try:
            tmp = int(digits)
        except Exception as e:
            return []

        res = []
        store = {
                "1": [],
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
        }
        def makeCombination(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    res.append("".join(cur))
                return

            for c in store[digits[i]]:
                cur.append(c)
                makeCombination(i+1, cur)
                cur.pop()

        makeCombination(0, [])
        return res


if __name__ == "__main__":

    solution = Solution()

    # recursive version test
    assert solution.letterCombinations_RECUR("") == []
    assert solution.letterCombinations_RECUR("xyz") == []
    assert solution.letterCombinations_RECUR("1") == []
    assert solution.letterCombinations_RECUR("2") == ["a", "b", "c"]
    # assert solution.letterCombinations_RECUR("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    tmp = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
            "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
            "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]

    assert solution.letterCombinations_RECUR("234") == tmp

