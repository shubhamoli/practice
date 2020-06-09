"""
    Leetcode 1301
"""


from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0:
            return False

        if len(s) == 0:
            return True

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False

    def isSubsequence_OPTI(self, s: str, t: str) -> bool:
        store = defaultdict(list)
        for i in range(len(t)):
            store[t[i]].append(i)


        start = 0
        for c in s:
            # if char c is not present in T
            if len(store[c]) == 0:
                return False

            # find index of start in store[c]
            # intially it'll 0 to get leftmost valye of c in store[c]
            # for next iteration it'll be at least +1 index than prev index of same character
            idx = bisect.bisect_left(store[c], start)

            # if no index is found for current of start in store[c]
            if idx == len(store[c]):
                return False

            # update start for next iteration
            start = store[c][idx] + 1

        return True




if __name__ == "__main__":

    solution = Solution()

    assert solution.isSubsequence("abc", "ahbgdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False

    assert solution.isSubsequence_OPTI("abc", "ahbgdc") == True
    assert solution.isSubsequence_OPTI("axc", "ahbgdc") == False

