"""
 1.1 - Implement an algorithm to determine whether a string has unique characters or not
       What if no other D.S can be used
"""


from collections import Counter


# First: by using another a DS (dict/Counter)
def checkUniqueCharactersUsingDS(s: str) -> bool:
    if not s:
        return False

    # This is our helper Data Structure
    # see: https://docs.python.org/2/library/collections.html#collections.Counter
    #
    # Space complexity o(1) as there will be fixed
    # charset. 128 for ASCII and so on so forth
    counter = Counter()

    # O(n)
    for i in s:
        # if character count is > 0
        # return false
        if counter[i]:
            return False

        counter.update(i)

    return True


# Second: without using any DS
def checkUniqueCharactersWithoutDS(s: str) -> bool:
    if not s:
        return False

    # O(nlogn)
    # O(n)
    # Python uses TimSort (see: https://en.wikipedia.org/wiki/Timsort)
    #
    # Also string in python are immutable
    # so can't be sorted in place
    # new string will be returned here, original string remains unchanged
    sorted_s = sorted(s)

    # O(n)
    # len() is O(1) operation in python
    for i in range(len(sorted_s)):
        if i+1 < len(sorted_s) and sorted_s[i+1] == sorted_s[i]:
            return False

    return True



if __name__ == "__main__":

    assert checkUniqueCharactersUsingDS("") == False
    assert checkUniqueCharactersUsingDS("a") == True
    assert checkUniqueCharactersUsingDS("aa") == False
    assert checkUniqueCharactersUsingDS("aab") == False
    assert checkUniqueCharactersUsingDS("abc") == True
    assert checkUniqueCharactersUsingDS("cabb") == False

    assert checkUniqueCharactersWithoutDS("") == False
    assert checkUniqueCharactersWithoutDS("a") == True
    assert checkUniqueCharactersWithoutDS("aa") == False
    assert checkUniqueCharactersWithoutDS("aab") == False
    assert checkUniqueCharactersWithoutDS("cab") == True
    assert checkUniqueCharactersWithoutDS("cabb") == False
    assert checkUniqueCharactersWithoutDS("abc") == True

