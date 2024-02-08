from llclass import LinkedList, Node


if __name__ == '__main__':
    ll = LinkedList(5)
    ll.push(1, 7, 22)
    ll.append(37)
    ll.print()
    print("length:", ll.len)

    ll.addIndex(100, 2)
    ll.print()
    print("length:", ll.len)

    lcyclic = LinkedList(1)
    lcyclic.head.next = Node(2, Node(3, Node(4, lcyclic.head)))
    print(lcyclic.is_cyclic())

    lshort = LinkedList(1)
    lshort.head.next = Node(2, lshort.head)
    print(lshort.is_cyclic())

    print(ll.is_cyclic())
