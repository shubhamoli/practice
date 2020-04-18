"""
    1.5 - Write a function to check if two strings are one edit (or zero edit) away
          edit == insert, delete or replace a character
"""


# Using brute force approach
def checkEditDistance(s1: str, s2: str) -> bool:

    # return False for more than 1 edit
    if abs(len(s1) - len(s2)) > 1:
        return False

    # remember len() is O(1) in Python
    if len(s1) == len(s2):
        # check for atmost 1 different character (Edit condition)
        found_diff = False

        # O(n)
        for i, j in zip(s1, s2):
            if i != j and found_diff:
                return False

            if i != j and not found_diff:
                found_diff = True

        return True

    # for length diff of 1
    # check only 1 character is less/extra in either string
    if abs(len(s1) - len(s2)) == 1:
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        i = 0
        j = 0

        # O(n)
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if i != j:
                    return False
                j += 1
            else:
                i += 1
                j += 1

        return True


if __name__ == "__main__":

    assert checkEditDistance("", "") == True
    assert checkEditDistance("pale", "ple") == True
    assert checkEditDistance("pale", "plf") == False
    assert checkEditDistance("", "pale") == False
    assert checkEditDistance("pale", "") == False
    assert checkEditDistance("pales", "pale") == True
    assert checkEditDistance("pales", "ple") == False
    assert checkEditDistance("pale", "bale") == True
    assert checkEditDistance("place", "pce") == False
    assert checkEditDistance("pale", "bake") == False
    assert checkEditDistance("pale", "pale") == True
