"""
Write a function `canConstruct(target, wordBank)` that accepts a target string and an
array of strings.

The function should return an int indicating how many combinations of words from the
wordbank can be constructed to form the target, if any.

You may reuse elements of wordBank as many times as needed.
"""


def canConstruct(target, wordbank, memo=None):
    """given an array of words in a wordbank, try construct the target word"""
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if not target:
        return 1

    count = 0
    for word in wordbank:
        if target.startswith(word):
            count += canConstruct(target[len(word) :], wordbank, memo)

    memo[target] = count
    return count


if __name__ == "__main__":
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))  # 3
    print(canConstruct("abcabdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(
        canConstruct("abcabbdef", ["ab", "abc", "cd", "def", "abcd"])
    )  # 0
    print(
        canConstruct("skateboard", ["bo", "ate", "rd", "t", "sk", "boar"])
    )  # 0
    print(
        canConstruct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            [
                "e",
                "ee",
                "eee",
                "eeee",
                "eeeee",
                "eeeeee",
            ],
        )
    )  # 0

"""
m = target length
n = wordbank length

Brute Force Solution
--------------------
O(n^m * m) time
O(m^2) space

Brute Force Solution
--------------------
O(n * m^2) time
O(m^2) space
"""
