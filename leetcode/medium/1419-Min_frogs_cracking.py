"""
    Leetcode #1419
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        store = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        res = 0

        for i in croakOfFrogs:
            store[i] += 1

            # freq of c, r, o, a, k should be monotonically decreasing
            if not (store['c'] >= store['r'] >= store['o'] >= store['a'] >= store['k']):
                return -1

            _max = max(store['c'], store['r'], store['o'], store['a'], store['k'])
            _min = min(store['c'], store['r'], store['o'], store['a'], store['k'])
            diff = _max - _min

            res = max(res, diff)

        # if croaks are not complete
        if not (store['c'] == store['r'] == store['o'] == store['a'] == store['k']):
            return -1

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.minNumberOfFrogs("croakcroak") == 1
    assert solution.minNumberOfFrogs("crcoakroak") == 2
    assert solution.minNumberOfFrogs("croakcrook") == -1
    assert solution.minNumberOfFrogs("croakcroa") == -1
