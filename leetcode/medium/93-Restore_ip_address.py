"""
    Leetcode #93
"""


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) < 4:
            return []

        res = []

        def helper(curr, idx):
            if idx == len(s) and len(curr) == 4:
                res.append(".".join(curr))
                return

            if len(curr) == 4 or idx > len(s):
                return

            for i in range(1, 4):
                tmp = s[idx:idx+i]
                if len(tmp) > 1 and tmp[0] == "0": continue

                if ( tmp and int(tmp) < 256 and int(tmp) >= 0 ):
                    curr.append(tmp)
                    helper(curr, i+idx)
                    curr.pop()

        helper([], 0)
        return res


if __name__ == "__main__":

    print(Solution().restoreIpAddresses("")) # []
    print(Solution().restoreIpAddresses("12")) # []

    print(Solution().restoreIpAddresses("25525511135")) # ["255.255.11.135", "255.255.111.35"]
    print(Solution().restoreIpAddresses("1111")) # ["255.255.11.135", "255.255.111.35"]
