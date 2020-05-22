"""
    Leetcode #451
"""

from collections import defaultdict, Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""

        counter = Counter(s)
        store = defaultdict(list)

        for k, v in counter.items():
            store[v].append(k*v)

        freq_arr = sorted(store.keys(), reverse=True)

        out = []
        for i in freq_arr:
            out.append("".join(store[i]))

        return "".join(out)

    def frequencySort_FASTER(self, s: str) -> str:
        s_set = set(s)
        table = []

        for val in s_set:
            table.append((val, s.count(val)))

        table.sort(key = lambda x: x[1], reverse = True) 

        return ''.join(map(lambda x: x[0] * x[1], table))


if __name__ == "__main__":

    solution = Solution()

    assert solution.frequencySort("tree") == "eetr"
    assert solution.frequencySort("cccaaa") == "cccaaa"
    assert solution.frequencySort("Aabb") == "bbAa"

