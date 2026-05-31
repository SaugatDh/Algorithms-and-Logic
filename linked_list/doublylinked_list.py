class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self,data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at(self,index,data):
        if index < 0  or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_first(data)
            return
        if index == self.size:
            self.insert_last(data)
            return
        new_node = Node(data)
        current = self._get_node_at(index)

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

        self.size += 1

    def _get_node_at(self,index):
        if index < self.size //2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        return current

    def find(self,target_value):
        current = self.head
        while current:
            if current.data == target_value:
                return current
            current = current.next
        return None

    def display_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("None <-> " + " <-> ".join(elements) + " <-> None")

    def display_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("None <-> " + " <-> ".join(elements) + " <-> None")

    def display(self):
            elements = []
            current = self.head
            while current:
                elements.append(str(current.data))
                current = current.next
            print("None <-> " + " <-> ".join(elements) + " <-> None")

    def delete_first(self):
        if self.head is None:
            return None
        data_to_return = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return data_to_return

    def delete_node(self,node_to_delete):
        if node_to_delete is None:
            return

        if node_to_delete == self.head:
            self.delete_first()
            return

        if node_to_delete == self.tail:
            self.delete_last()
            return

        node_to_delete.prev.next = node_to_delete.next
        node_to_delete.next.prev = node_to_delete.prev

        self.size -= 1
        return node_to_delete.data

    def delete_last(self):
        if self.tail is None:
            return None
        data_to_return = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data_to_return

dll = DoublyLinkedList()

dll.insert_first(20)
dll.insert_first(10)
dll.insert_last(30)
dll.insert_at(2, 25)

dll.display_forward()

dll.display_backward()

dll.delete_first()
dll.delete_last()

target_node = dll.find(25)
dll.delete_node(target_node)

dll.display_forward()
