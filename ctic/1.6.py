"""
    1.6 - Write a function to compress string. For "aabbbcccc" it should return "a2b3c4"
          String can only contain uppercase and lowercase character
"""


def compressStr(s: str) -> str:

    if not s:
        return ""

    # aabbccaa -> aaaabbcc
    # O(nlogn)
    sorted_s = sorted(s)

    res = []

    tmp = sorted_s[0]
    res.append(tmp)

    count = 0

    # O(n)
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == tmp:
            count += 1
        else:
            if count: res.append(str(count+1))

            # Start tracking new value
            tmp = sorted_s[i]
            res.append(tmp)

            # reset counter
            count = 0

    if count:
        res.append(str(count+1))

    return "".join(res)




if __name__ == "__main__":

    assert compressStr("") == ""
    assert compressStr("a") == "a"
    assert compressStr("ab") == "ab"
    assert compressStr("abc") == "abc"
    assert compressStr("aa") == "a2"
    assert compressStr("aaab") == "a3b"
    assert compressStr("aabbbccccaaa") == "a5b3c4"

