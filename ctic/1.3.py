"""
    1.3 - Write a function to replace all spaces in a string with "%20"
"""


# O(n^2)
def URLify(s: str) -> str:
    # remove extra whitespaces
    # O(n)
    s = s.strip()

    res = ""

    # O(n^2)
    # as strings are immutable in python
    # so every time we have to copy string to res which itself O(n)
    for i in s:
        if i == " ":
            res += "%20"
        else:
            res += i

    return res


# O(n)
def URLifyOptimized(s: str) -> str:
    # remove extra whitespaces
    # O(n)
    s = s.strip()

    res = []

    # O(n)
    # as list.append() is O(1)
    for i in s:
        if i == " ":
            res.append("%20")
        else:
            res.append(i)

    # O(n)
    #
    # CPython Implementation:
    # join() just allocats memory one time (length of iterable) to copy string
    # where simple + concatenation copies string on each iteration
    return "".join(res)


if __name__ == "__main__":

    assert URLify("") == ""
    assert URLify("ab") == "ab"
    assert URLify("a b c") == "a%20b%20c"
    assert URLify("ab c") == "ab%20c"
    assert URLify("   abc   ") == "abc"
    assert URLify("   a b c") == "a%20b%20c"

    assert URLifyOptimized("") == ""
    assert URLifyOptimized("ab") == "ab"
    assert URLifyOptimized("a b c") == "a%20b%20c"
    assert URLifyOptimized("ab c") == "ab%20c"
    assert URLifyOptimized("   abc   ") == "abc"
    assert URLifyOptimized("   a b c") == "a%20b%20c"

