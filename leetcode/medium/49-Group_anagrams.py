"""
    Leetcode #49
"""


from typing import List
from collections import Counter


class Solution:
    # Brute force
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        def checkAnagrams(a: str, b: str):
            if len(a) != len(b):
                return False

            counter = Counter(a)

            for j in b:
                counter[j] -= 1

            for c in counter:
                if counter[c] > 0:
                    return False

            return True

        used = {}
        for i in range(len(strs)):
            if used.get(strs[i]): continue

            j = i+1
            curr = []
            curr.append(strs[i])
            while j < len(strs):
                if len(strs[i]) == len(strs[j]) and checkAnagrams(strs[i], strs[j]):
                    used[strs[j]] = True
                    curr.append(strs[j])
                j += 1

            res.append(curr)

        return res


    def groupAnagrams_OPTI(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        res = {}
        for i in strs:
            s = "".join(sorted(i))  # O(nlogn)
            if res.get(s):
                res[s].append(i)
            else:
                res[s] = [i]

        return [res[x] for x in res]



if __name__ == "__main__":

    solution = Solution()

    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams_OPTI(["eat", "tea", "tan", "ate", "nat", "bat"]))
