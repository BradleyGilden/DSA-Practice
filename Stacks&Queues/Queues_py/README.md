# Queues (FIFO)

<img src ="resources/queue.png">

Queues are linear data structures that follow *FIFO* order (First In, First Out). Insertion is done at the rear (enqueue) and deletion is done at the front (dequeue).

## Primary Operations

* Enqueue: adds new item to the start of the list
  * if queue is full, there is an overflow condition

* Dequeue: removes item at the end of the list
  * if queue is empty, there is an underflow condition

Other possible operations include: Peek, IsEmpty, Clear, Size

## Types of Queues:

* Circular Queues
  * Queue in which last element points to first element
  * Also known as Ring Buffer
  * insertion is at the rear, deletion is at the front
* Doubly-ended Queues
  * Queue in which both insertion and deletion operations are done at the rear and front
* Priority Queues
  * Elements have predefined priority
  * Elements with the highest priority are dequeued first
  * Elements are inserted with priority in mind and are stored as such.
