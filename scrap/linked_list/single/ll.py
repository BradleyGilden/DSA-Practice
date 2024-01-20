from llclass import LinkedList


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.push(1, 7, 22)
    ll.append(37)
    ll.print()
    print("length:", ll.len)

    ll.addIndex(100, 2)
    ll.print()
    print("length:", ll.len)
