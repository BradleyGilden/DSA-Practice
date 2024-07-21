"""
Write a function `canConstruct(target, wordBank)` that accepts a target string and an
array of strings.

The function should return a boolean indicating whether or not the `target` can
be constructed by concatenating elements of the `wordBank` array.

You may reuse elements of wordBank as many times as needed.
"""


def canConstruct(target, wordbank, memo=None):
    """given an array of words in a wordbank, try construct the target word
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if not target:
        return True
    
    for word in wordbank:
        newTarget = target
        if target.startswith(word):
            newTarget = target[len(word):]
            if canConstruct(newTarget, wordbank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


if __name__ == '__main__':
    print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # true
    print(canConstruct('abcabdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # true
    print(canConstruct('abcabbdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # false
    print(canConstruct('skateboard', ['bo', 'ate', 'rd', 't', 'sk', 'boar']))  # false
    print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
    ]))