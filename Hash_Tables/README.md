# Hash tables

Hashtables (also known as hash maps) is a data structure that provides efficient storage and retrieval of key-value pairs, allowing for fast access to data based on its unique key.

## Directory Files

## How Hash tables function (in theory)

* A hash table is essentially an array of slots, where each slot can hold one key-value pair.

* The key is used to calculate a hash code, which is an integer value that represents the key

* The hash code is then mapped to an index within the array, known as the hash function.

* The hash function takes the hash code and converts it into an index within the array. See [djb2](/algorithms/DJB2.md) for a hash function algorithm

* Ideally, the hash function should distribute the keys uniformly across the array, minimizing collisions (situations where two keys map to the same index). However, collisions are inevitable due to the limited size of the array compared to the potentially infinite number of keys.

* To handle collisions, most hash table implementations use a technique called chaining. In chaining, each slot in the array holds a linked list or some other data structure that can store multiple key-value pairs

* When a collision occurs, the new key-value pair is appended to the list at that slot. This way, multiple key-value pairs can coexist at the same index

* When retrieving a value from a hash table, the key is hashed again to determine the corresponding index. The hash table then follows the linked list (or any other data structure) at that index to find the desired value

* In the best-case scenario, with a good hash function and minimal collisions, the retrieval time is constant, O(1). However, in the worst-case scenario, with many collisions, the retrieval time can approach O(n), where n is the total number of key-value pairs.

## Summary

* used to index large amounts of data

* address of each key is calculated using the key itself

* collisions resolved with open or closed addressing

* hashing is widely used in database indexing, compilers, caching, password authentication, and more.
