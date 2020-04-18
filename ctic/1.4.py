"""
    1.4 - Write a function to check if a string is permutation of a palindrome.
          Palindrome doesn't need to be limited to dictionary word (it can be any random word without meaning)
"""


from collections import Counter


# so basically we have to check whether
# this string has qualities of a palindrom or not
def checkPermutationOfPalindrome(s: str) -> bool:

    # let's make all characater lower case
    # for simplicity
    lower = s.lower()

    # avoided for-loop here by passing string in constructor
    counter = Counter(lower)

    # All character should have even no. of occurences
    # except 1 other character middle can have maiden occurence
    odd_encountered = False

    for j in counter:
        # For even no. of chars do nothing
        if counter[j] % 2 == 0:
            continue

        if j != " " and counter[j] % 2 != 0:
            # not more than 1 character with odd occurences are permitted
            if odd_encountered:
                return False

            odd_encountered = True

    return True

if __name__ == "__main__":

    assert checkPermutationOfPalindrome("Tact Coa") == True
    assert checkPermutationOfPalindrome("TaccCoa") == False
    assert checkPermutationOfPalindrome("TactCoa") == True
    assert checkPermutationOfPalindrome("TactT CoTa") == True
    assert checkPermutationOfPalindrome("") == True

