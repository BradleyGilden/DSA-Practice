class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):  # add data at the beginning of list
        new_node = Node(data)
        new_node.next = None
        new_node.prev = None
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def view(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def dequeue(self):
        if self.tail is None:
            return
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        temp.prev = None
        self.size -= 1

    def peek_start(self):
        if self.head is not None:
            print(self.head.data)

    def peek_end(self):
        if self.tail is not None:
            print(self.tail.data)

    def isEmpty(self):
        if self.head is not None:
            print("List has contents")
        else:
            print("List is empty")

    def Size(self):
        return self.size
