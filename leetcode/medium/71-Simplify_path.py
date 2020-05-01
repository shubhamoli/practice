"""
    Leetcode #71
"""


class Solution():
    def simplifyPath(self, path: str) -> str:
        res = []
        path = path.split('/')

        for i in path:
            if(i == ''):
                continue
            elif(i == '.'):
                continue
            elif(i == '..'):
                if(len(res)):
                    res.pop()
            else:
                res.append('/'+i)

        if(len(res) == 0):
            res.append('/')

        return "".join(res)


if __name__ == "__main__":

    solution = Solution()

    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/home//foo/") == "/home/foo"
    assert solution.simplifyPath("/a/./b/../../c/") == "/c"
    assert solution.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
