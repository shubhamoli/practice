"""
    Leetcode #438
"""


from typing import List
from collections import Counter, deque


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []

        if not p:
            return [0]


        res = []
        counter_p = Counter(p)
        counter_s = Counter(s[0:len(p)-1])

        for i in range(len(p)-1, len(s)):
            counter_s[s[i]] += 1
            if counter_s == counter_p:
                res.append(i-len(p)+1)

            # decrease count for first character
            counter_s[s[i-len(p)+1]] -= 1
            if counter_s[s[i-len(p)+1]] == 0:
                del counter_s[s[i-len(p)+1]]

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2]

