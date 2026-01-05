"""
Write a function `allConstruct(target, wordBank)` that accepts a target string
and an array of strings.

The function should return a 2D array containing all of the ways that the `target` can
be constructed by concatenating elements of the `wordBank` array. Each element of the 2D array
should represent one combination that constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.
"""

from pprint import pprint


def allConstruct(target, wordbank, memo=None):
    """Given an array of words in a wordbank, try to construct the target word."""
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if not target:
        return [[]]

    comb_list = []
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = allConstruct(suffix, wordbank, memo)
            target_ways = [[word] + way for way in suffix_ways]
            comb_list.extend(target_ways)

    memo[target] = comb_list
    return comb_list


if __name__ == "__main__":
    pprint(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
    # pprint(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # pprint(allConstruct("abcabdef", ["ab", "abc", "cd", "def", "abcd"]))
    # pprint(
    #     allConstruct("abcabbdef", ["ab", "abc", "cd", "def", "abcd"])
    # )
    # pprint(
    #     allConstruct("skateboard", ["bo", "ate", "rd", "t", "sk", "boar"])
    # )
    # pprint(
    #     allConstruct(
    #         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    #         [
    #             "e",
    #             "ee",
    #             "eee",
    #             "eeee",
    #             "eeeee",
    #             "eeeeee",
    #         ],
    #     )
    # )
