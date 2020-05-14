"""
    Leetcode #165
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')

        max_len = max(len(s1),len(s2))
        s1 = self.zeroPadding(s1,max_len)
        s2 = self.zeroPadding(s2,max_len)
        i = 0

        while i < len(s1) and i<len(s2):
            if int(s1[i])== int(s2[i]):
                i += 1
            elif int(s1[i]) > int(s2[i]):
                return 1
            else:
                return -1
        return 0

    def zeroPadding(self,s,max_len):
        if len(s) < max_len:
            return s + [0] * (max_len -len(s))
        return s


if __name__ == "__main__":

    assert Solution().compareVersion("0.1", "1.1") == -1
    assert Solution().compareVersion("1.0.1", "1") == 1
    assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1
    assert Solution().compareVersion("1.0.0", "1.0") == 0

