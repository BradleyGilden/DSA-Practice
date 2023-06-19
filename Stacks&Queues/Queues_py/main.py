from queue import Queue


if __name__ == '__main__':
    que = Queue()
    que.enqueue("Arthur")
    que.enqueue("Ron")
    que.enqueue("Fred")
    que.enqueue("George")
    que.enqueue("Molly")
    que.enqueue("Bill")
    que.enqueue("Charlie")
    que.enqueue("Ginny")
    que.dequeue()
    que.view()
    print()
    que.peek_start()
    que.peek_end()
    que.isEmpty()
    print(que.Size())
