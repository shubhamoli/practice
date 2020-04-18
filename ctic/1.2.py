"""
    1.2 - Given two strings, write a function to decide whether
          One is permutation of another or not
"""


# Assuming case-sensitive permutation check
# 'god' is permutation of 'dog', where `God` is not
def checkPermutation(s1: str, s2: str) -> bool:

    # O(n) in both time and space
    s1 = s1.strip()
    s2 = s2.strip()

    # String of diff length can't be permutation of each other
    if len(s1) != len(s2):
        return False

    # 2 * O(n)
    set1 = set(s1)
    set2 = set(s2)

    # set in python are equal if they contain same elements
    # not necessarily in same order
    #
    # O(n)
    if set1 != set2:
        return False

    return True



if __name__ == "__main__":

    assert checkPermutation("", "") == True
    assert checkPermutation("abc", "") == False
    assert checkPermutation("aaaaa", "aaa") == False    # not same length
    assert checkPermutation("abac", "abca") == True
    assert checkPermutation("      abac     ", "abca") == True
    assert checkPermutation("testing", "gnitset") == True
    assert checkPermutation("abc", "def") == False
