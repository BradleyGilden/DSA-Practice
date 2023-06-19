from stack import Stack


if __name__ == '__main__':
    mylist = Stack()
    mylist.isEmpty()
    mylist.push("Hydrogen")
    mylist.push("Helium")
    mylist.push("Berylium")
    mylist.push("Boron")
    mylist.push("Gold")
    mylist.push("Magnesium")
    popped = mylist.pop()
    print(popped.data)
    peeked = mylist.peek()
    print(peeked)
    mylist.isEmpty()
    print(mylist.get_size())
