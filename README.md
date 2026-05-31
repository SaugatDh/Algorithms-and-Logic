# Algorithms and Logic

A collection of fundamental Data Structures and Algorithms (DSA) implemented in Python. Covers core topics from MIT 6.006-style curriculum including arrays, linked lists, stacks, queues, hash tables, sets, and search algorithms.

## Project Structure

```
Algorithms and logic/
├── array_seq/              # Static array sequence
├── Dynamic_array /         # Dynamic array with auto-resizing
├── linked_list/            # Singly linked list
├── stack/                  # Stack (array-based + linked list-based)
├── Queue/                  # Queue using linked list
├── Hash_table/             # Hash table (linear probing + separate chaining)
├── Set_from_Seq/           # Set ADT built on sequence
└── search operations/      # Linear search & binary search
```

---

## Data Structures

### 1. Static Array Sequence

**File:** `array_seq/array_seq.py`

Fixed-size array wrapper implementing a sequence interface.

| Operation | Time Complexity |
|---|---|
| `get_at(i)` / `set_at(i, x)` | O(1) |
| `insert_at(i, x)` | O(n) |
| `delete_at(i)` | O(n) |
| `insert_first(x)` / `delete_first()` | O(n) |
| `insert_last(x)` / `delete_last()` | O(n) |

**Key concepts:** Element shifting on insert/delete, forward/backward copy helpers.

---

### 2. Dynamic Array

**Files:** `Dynamic_array /dynamic_array.py`, `Set_from_Seq/dynamic_array.py`

Extends the static array with automatic resizing (grow/shrink by factor of 2).

| Operation | Time Complexity |
|---|---|
| `get_at(i)` / `set_at(i, x)` | O(1) |
| `insert_last(x)` | O(1) amortized |
| `delete_last()` | O(1) amortized |
| `insert_at(i, x)` / `delete_at(i)` | O(n) |
| `insert_first(x)` / `delete_first()` | O(n) |

**Key concepts:** Amortized analysis, upper/lower bound resizing, load factor management.

---

### 3. Singly Linked List

**Files:** `linked_list/linked_list.py`, `linked_list/mit_linkedlist.py`

Two implementations: a basic procedural version and a full-featured MIT 6.006-style sequence class.

| Operation | Time Complexity |
|---|---|
| `insert_first(x)` / `delete_first()` | O(1) |
| `get_at(i)` / `set_at(i, x)` | O(i) |
| `insert_at(i, x)` / `delete_at(i)` | O(i) |
| `insert_last(x)` / `delete_last()` | O(n) |
| `traverse()` | O(n) |
| `find_min()` | O(n) |

**Key concepts:** Node-based storage, pointer manipulation, traversal, index-based access via `later_node(i)`.

---

### 4. Stack (LIFO)

**Files:** `stack/stack.py`, `stack/stack_using_linkedlist.py`

Two implementations: one backed by a Python list (array-based), one backed by a linked list.

| Operation | Array-based | Linked List-based |
|---|---|---|
| `push(x)` | O(1)* | O(1) |
| `pop()` | O(1)* | O(1) |
| `peek()` | O(1) | O(1) |
| `isEmpty()` | O(1) | O(1) |
| `size()` | O(1) | O(1) |

*Amortized for array-based due to Python list resizing.

**Key concepts:** LIFO ordering, push/pop/peek, head-of-list insertion for linked list variant.

---

### 5. Queue (FIFO)

**File:** `Queue/queue.py`

Implemented using a singly linked list with front and rear pointers.

| Operation | Time Complexity |
|---|---|
| `enqueue(element)` | O(1) |
| `dequeue()` | O(1) |
| `peek()` | O(1) |
| `isEmpty()` | O(1) |
| `size()` | O(1) |

**Key concepts:** FIFO ordering, front/rear pointer management, O(1) enqueue and dequeue.

---

### 6. Hash Table

**Files:** `Hash_table/hash_table.py`, `Hash_table/hashtable.py`, `Hash_table/hash_table_rp.ipynb`

Three implementations covering different collision resolution strategies:

#### a) Linear Probing (`hash_table.py`)
- Open addressing with tombstone markers for lazy deletion
- Auto-resize: grow at load factor >= 0.6, shrink at <= 0.2
- Full dict-like interface (`__setitem__`, `__getitem__`, `__delitem__`)
- Insertion order tracking

#### b) Separate Chaining (`hashtable.py`)
- Fixed-size table with each bucket as a Python list
- Simple hash function summing ASCII values modulo table size

#### c) Jupyter Notebook (`hash_table_rp.ipynb`)
- Step-by-step development from basic hash functions to full hash table class
- Covers: direct mapping, separate chaining, load factor, dynamic resizing

| Operation | Average Case | Worst Case |
|---|---|---|
| `insert` | O(1) | O(n) |
| `lookup` | O(1) | O(n) |
| `delete` | O(1) | O(n) |

**Key concepts:** Hash functions, collision resolution (linear probing, separate chaining), load factor, dynamic resizing, amortized O(1) operations.

---

### 7. Set (Abstract Data Type)

**File:** `Set_from_Seq/set_from_seq.py`

Generic Set ADT built on top of any sequence implementation using a factory pattern (dependency injection).

| Operation | Time Complexity |
|---|---|
| `build(A)` | O(n) |
| `insert(x)` | O(n) |
| `delete(k)` | O(n) |
| `find(k)` | O(n) |
| `find_min()` | O(n) |
| `find_max()` | O(n) |
| `find_next(k)` | O(n) |
| `find_prev(k)` | O(n) |
| `iter_ord()` | O(n log n) |

**Key concepts:** Key-based comparison, factory/generic pattern, sorted iteration via repeated `find_min` + `find_next`.

---

## Algorithms

### 1. Linear Search

**File:** `search operations/linear_search.py`

Sequential scan through an unsorted array checking each element.

| Metric | Value |
|---|---|
| Time Complexity | O(n) |
| Space Complexity | O(1) |
| Sorted Array Required | No |

Tracks the number of comparisons made during search.

---

### 2. Binary Search

**File:** `search operations/binary_search.py`

Divide-and-conquer search on a sorted array, repeatedly halving the search space.

| Metric | Value |
|---|---|
| Time Complexity | O(log n) |
| Space Complexity | O(1) |
| Sorted Array Required | Yes |

Tracks comparisons made and measures execution time using `time.perf_counter()`.

---

## Running the Code

Each module is self-contained and can be run independently:

```bash
# Static array
python array_seq/array_seq.py

# Dynamic array
python "Dynamic_array /dynamic_array.py"

# Linked list
python linked_list/linked_list.py
python linked_list/mit_linkedlist.py

# Stack
python stack/stack.py
python stack/stack_using_linkedlist.py

# Queue
python Queue/queue.py

# Hash table
python Hash_table/hash_table.py
python Hash_table/hashtable.py

# Set from sequence
python Set_from_Seq/set_from_seq.py

# Search algorithms
python "search operations/linear_search.py"
python "search operations/binary_search.py"
```

## Topics Summary

| Category | Topics Covered |
|---|---|
| **Arrays** | Static Array, Dynamic Array (amortized resizing) |
| **Linked Structures** | Singly Linked List |
| **Stacks** | Array-based, Linked List-based |
| **Queues** | Linked List-based |
| **Hashing** | Linear Probing, Separate Chaining, Dynamic Resizing |
| **Sets** | Generic Set ADT (factory pattern) |
| **Search** | Linear Search O(n), Binary Search O(log n) |

## License

Apache License 2.0
