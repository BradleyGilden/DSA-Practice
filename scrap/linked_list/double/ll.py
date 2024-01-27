from llclass import LinkedList


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.push(1, 7, 22)
    ll.append(9, 45, 3)
    ll.print()
    print("length:", ll.len)

    print()
    print("adding 100 at index 6:")
    ll.addIndex(100, 6)
    ll.print()
    print("length:", ll.len)

    print()
    print("swapping head and tail")
    ll.swap(ll.tail, ll.head)
    ll.print()

    llcopy = ll.clone()
    print()
    print("a copied linked list")
    print("original: ", end="")
    ll.print()
    print("copy:     ", end="")
    llcopy.print()

    print()
    print("delete node at index")
    print("original: ", end="")
    llcopy.print()
    print(f"deleted {llcopy.delete(2)} at index 2: ", end="")
    llcopy.print()

    print()
    print("sorting using bubble sort")
    ll.bubble_sort()
    ll.print()
