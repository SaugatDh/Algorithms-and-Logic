#%%
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    if head is None or head.data is None:
        print("null")
        return
    currentNode = head 
    while currentNode:
        print(currentNode.data,end=" -> ")
        currentNode = currentNode.next
    print("null")

def deleteSpecificNode(head,nodeToDelete):
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head
    currentNode.next = currentNode.next.next
    return head

# Inserting a Node in a linked list
def insertNodeAtPosition(head,newNode,position):
    if position == 1:
        newNode.next = head
    currentNode = head
    for _ in range(position - 2):
        if currentNode.next is None:
            break
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next =newNode
    return head
# find lowest value in a linked list

def findLowestValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

#%%
node1 = Node(6)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print("Before deletion:")
# traverseAndPrint(node1)

# # Delete node4
# node1 = deleteSpecificNode(node1, node4)

# print("\nAfter deletion:")
# traverseAndPrint(node1) 
#%%
print("The lowest value in the linked list is:", findLowestValue(node1)) 
# def main():
#     node1 = Node()
#     traverseAndPrint(node1)

# if __name__ == "__main__":
#     main()