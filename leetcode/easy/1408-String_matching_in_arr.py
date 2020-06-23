"""
    Leetcode #1408
"""


from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words:
            return []

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break   # avoid repeating elements

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.stringMatching(["mass","as","hero","superhero"]) == ["as", "hero"]
    assert solution.stringMatching(["leetcode","et","code"]) == ["et","code"]
