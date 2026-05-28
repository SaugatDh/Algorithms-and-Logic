#%%
class Node:
    def __init__(self,x):
        self.item = x
        self.next = None

    def later_node(self,i):
        current = self
        for _ in range(i):
            if current.next is None:
                raise IndexError("Linked List index out of range.")
            current = current.next
        return current

class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self,X):
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self,i):
        if i<0 or i>=self.size:
            raise IndexError("Linked List index out of range.")
        node = self.head.later_node(i)
        return node.item

    def set_at(self,i,x):
        if i<0 or i>=self.size:
            raise IndexError("Linked List index out of range.")
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise IndexError("Cannot delete from an empty linked list.")
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self,i,x):
        if i<0 or i>self.size:
            raise IndexError("Linked List index out of range.")
        if i == 0:
            self.insert_first(x)
            return
        new_node = Node(x)
        pred_node = self.head.later_node(i-1)
        new_node.next = pred_node.next
        pred_node.next = new_node
        self.size += 1
    def delete_at(self,i):
        if i<0 or i>=self.size:
            raise IndexError("Linked List index out of range.")
        if i == 0:
            return self.delete_first()

        pred_node = self.head.later_node(i-1)
        target_node = pred_node.next
        x=target_node.item

        pred_node.next = target_node.next
        self.size -= 1
        return x
    def insert_last(self,x):
        self.insert_at(self.size,x)
    def delete_last(self):
        return self.delete_at(self.size-1)
#%%
# --- Verification ---
if __name__ == "__main__":
    print("--- 1. Testing Initialization & __len__ ---")
    li = Linked_List_Seq()
    print(f"Empty list contents: {list(li)}")
    print(f"Empty list length: {len(li)}")  # Expected: 0
    print("-" * 50)

    print("--- 2. Testing build() & __iter__ ---")
    dataset = [6, 2, 3, 4, 0]
    print(f"Building list from native array: {dataset}")
    li.build(dataset)
    print(f"Verified via __iter__: {list(li)}")  # Expected: [6, 2, 3, 4, 0]
    print(f"Verified length: {len(li)}")        # Expected: 5
    print("-" * 50)

    print("--- 3. Testing get_at() & set_at() ---")
    print(f"Current list: {list(li)}")
    val_at_2 = li.get_at(2)
    print(f"Item at index 2: {val_at_2}")  # Expected: 3

    print("Modifying index 2 to have value 99...")
    li.set_at(2, 99)
    print(f"Updated list: {list(li)}")      # Expected: [6, 2, 99, 4, 0]
    print("-" * 50)

    print("--- 4. Testing insert_first() ---")
    print(f"Before insertion: {list(li)}")
    li.insert_first(11)
    print(f"After inserting 11 at front: {list(li)}")  # Expected: [11, 6, 2, 99, 4, 0]
    print(f"New length: {len(li)}")                    # Expected: 6
    print("-" * 50)

    print("--- 5. Testing delete_first() ---")
    print(f"Before deletion: {list(li)}")
    deleted_head = li.delete_first()
    print(f"Deleted value: {deleted_head}")            # Expected: 11
    print(f"After deleting front element: {list(li)}") # Expected: [6, 2, 99, 4, 0]
    print(f"New length: {len(li)}")                     # Expected: 5
    print("-" * 50)

    print("--- 6. Testing insert_at() ---")
    print(f"Before structural insertion: {list(li)}")
    # Inserting 55 at index 3 (between 99 and 4)
    li.insert_at(3, 55)
    print(f"After inserting 55 at index 3: {list(li)}") # Expected: [6, 2, 99, 55, 4, 0]
    print(f"New length: {len(li)}")                      # Expected: 6
    print("-" * 50)

    # ----------------------------------------------------------------
    # 7. Test: delete_at()
    # ----------------------------------------------------------------
    print("--- 7. Testing delete_at() ---")
    print(f"Before structural deletion: {list(li)}")
    # Deleting index 2 (value 99)
    deleted_mid = li.delete_at(2)
    print(f"Deleted value from index 2: {deleted_mid}")  # Expected: 99
    print(f"After deleting index 2: {list(li)}")          # Expected: [6, 2, 55, 4, 0]
    print(f"New length: {len(li)}")                       # Expected: 5
    print("-" * 50)

    # ----------------------------------------------------------------
    # 8. Test: insert_last()
    # ----------------------------------------------------------------
    print("--- 8. Testing insert_last() ---")
    print(f"Before appending: {list(li)}")
    li.insert_last(88)
    print(f"After appending 88 to tail: {list(li)}")  # Expected: [6, 2, 55, 4, 0, 88]
    print(f"New length: {len(li)}")                    # Expected: 6
    print("-" * 50)

    # ----------------------------------------------------------------
    # 9. Test: delete_last()
    # ----------------------------------------------------------------
    print("--- 9. Testing delete_last() ---")
    print(f"Before popping tail: {list(li)}")
    deleted_tail = li.delete_last()
    print(f"Deleted value from tail: {deleted_tail}")  # Expected: 88
    print(f"After removing tail element: {list(li)}")  # Expected: [6, 2, 55, 4, 0]
    print(f"Final length: {len(li)}")                   # Expected: 5
    print("-" * 50)

    # ----------------------------------------------------------------
    # 10. Test: Defensive Guardrails & Index Errors
    # ----------------------------------------------------------------
    print("--- 10. Testing Bounds Checking (Defensive Exceptions) ---")
    print("Attempting to read out-of-bounds index 99...")
    try:
        li.get_at(99)
    except IndexError as e:
        print(f"Successfully caught expected error: {e}")

    print("\nAttempting to delete from an out-of-bounds negative index...")
    try:
        li.delete_at(-1)
    except IndexError as e:
        print(f"Successfully caught expected error: {e}")
        
    print("\n==================================================")
    print("          ALL STRUCTURAL TESTS COMPLETE           ")
    print("==================================================")