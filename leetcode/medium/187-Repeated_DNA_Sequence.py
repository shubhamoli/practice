"""
    Leetcode #187
"""


from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s:
            return []

        store = {}

        for i in range(len(s)-9):
            tmp = s[i:i+10]

            # means found more than once
            if store.get(tmp) is not None:
                store[tmp] += 1
            else:
                store[tmp] = 1

        return [i for i in store if store[i] > 1]



if __name__ == "__main__":


    assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"]
