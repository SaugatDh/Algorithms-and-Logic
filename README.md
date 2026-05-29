# Algorithms-and-Logic

A collection of fundamental Data Structures and Algorithms (DSA) implemented in Python.

## Project Structure

```
Algorithms and logic/
├── array_seq/              # Array sequence implementation
├── binary_search           # Binary search (C implementation)
├── binary_search.c         # Binary search in C
├── Dynamic_array /         # Dynamic array with resizing
├── Hash_table/             # Hash table with linear probing
├── linked_list/            # Linked list operations
├── Queue/                  # Queue using linked list
├── search operations/      # Search algorithms
├── Set_from_Seq/           # Set implementation from sequence
└── stack/                  # Stack implementations
```

## Data Structures

### Array Sequence
Basic array sequence with insert, delete, and access operations.

### Dynamic Array
Resizable array implementation with automatic capacity management. Supports:
- Insert/delete at any position
- Automatic resizing based on load factor

### Linked List
Singly linked list with:
- Node traversal and printing
- Insert/delete operations
- Find minimum value

### Stack
LIFO (Last In, First Out) data structure with:
- `push(element)` - Add element to top
- `pop()` - Remove and return top element
- `peek()` - View top element without removing
- `isEmpty()` - Check if stack is empty
- `size()` - Get number of elements

### Queue
FIFO (First In, First Out) data structure using linked list:
- `enqueue(element)` - Add element to rear
- `dequeue()` - Remove and return front element
- `peek()` - View front element without removing
- `isEmpty()` - Check if queue is empty
- `size()` - Get number of elements

### Hash Table
Hash table implementation with linear probing for collision resolution:
- Automatic resizing when load factor exceeds 0.6
- Shrink when load factor drops below 0.2
- Full dict-like interface (`__setitem__`, `__getitem__`, `__delitem__`)
- Methods: `get()`, `pop()`, `update()`, `setdefault()`, `clear()`

### Set from Sequence
Set implementation built on top of the array sequence.

## Algorithms

### Linear Search
O(n) search algorithm that checks each element sequentially.

### Binary Search
O(log n) search algorithm for sorted arrays (implemented in both Python and C).

## Running the Code

Each module can be run independently:

```bash
# Run stack implementation
python stack/stack.py

# Run queue implementation
python Queue/queue.py

# Run hash table
python Hash_table/hash_table.py

# Run linked list
python linked_list/linked_list.py
```

## License

Apache License 2.0
