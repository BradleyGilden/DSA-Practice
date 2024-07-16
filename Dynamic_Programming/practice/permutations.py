from pprint import pprint


def permutations(items):
    permList = []
    size = len(items)

    def generate_perm(items, perm=[]):
        if len(perm) == size:
            permList.append(perm[:])
            return

        for item in items:
            if item not in perm:
                perm.append(item)
                generate_perm(items, perm)
                perm.pop()

    generate_perm(items)

    return permList


if __name__ == '__main__':
    pprint(permutations(['a', 'b', 'c']))
