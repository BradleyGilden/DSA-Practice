# Single Linked Lists properties

* Navigation is Forward only
* A linked list made up of **nodes** containging: Data and Link
  * ```
    +--------+--------+          +--------+--------+
    |  Data  |  Link  | --next-->|  Data  |  Link  |
	+--------+--------+          +--------+--------+ 
	       Node1						Node2
	```

* Each node contains data of a specific type and a link pointing to the next node in list. The link of the last node will point to NULL.
  * ```
    +--------+--------+          +--------+--------+
    |  Data  |  2000  | --next-->|  Data  |  NULL  |
	+--------+--------+          +--------+--------+ 
	  address:  1000  				address: 2000
	```
* We can use a **Head** pointer to point to the first node of the list
  * ```
    +--------+--------+          +--------+--------+
    |  Data  |  2000  | --next-->|  Data  |  NULL  |
	+--------+--------+          +--------+--------+ 
	  1000  				        2000
	    ↑
	+--------+
    |  1000  |
    +--------+
	   Head
	
	```
* Unlike arrays which are sequential in memory (e.g int array: 1000->1004->1008), liked lists are linked to scattered locations in memory (e.g int linked list: 1004->2508->988)

## When To Use Linked Lists vs Arrays

| Linked Lists | Arrays |
|:-------------|:-------|
| 1. You need constant-time insertions/deletions from the list (such as in real-time computing where time predictability is absolutely critical) | 1. You need indexed/random access to elements |
| 2. You don't know how many items will be in the list. With arrays, you may need to re-declare and copy memory if the array grows too big | 2. You know the number of elements in the array ahead of time so that you can allocate the correct amount of memory for the array |
| 3. You don't need random access to any elements  | 3. You need speed when iterating through all the elements in sequence. You can use pointer math on the array to access each element, whereas you need to lookup the node based on the pointer for each element in linked list, which may result in page faults which may result in performance hits. |
| 4. You want to be able to insert items in the middle of the list (such as a priority queue) | 4. Memory is a concern. Filled arrays take up less memory than linked lists. Each element in the array is just the data. Each linked list node requires the data as well as one (or more) pointers to the other elements in the linked list. |
