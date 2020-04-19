"""
    1.8 - Check whether s2 is rotation of s1 with one call to isSubstring()
"""


def checkRotation(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False

    # strings of diff length can't be rotation of each other
    if len(s1) != len(s2):
        return False

    # x (one half) and y (other half)
    # xyxy will always contain yx (rotation)
    #
    # O(n)
    return s2 in (s1+s1)


if __name__ == "__main__":

    assert checkRotation("", "") == False
    assert checkRotation("hello", "llohe") == True
    assert checkRotation("hello", "lloeh") == False
