# STACK
# Last in first out,
# When using a list, pop takes out the last element in the list because
# you append (at the back) to a list
class UseStack():
    def __init__(self):
        self.items = []
    def push(self, item):
        print("ADDING ", item, "INTO STACK")
        self.items.append(item)
    def pop(self):
        if len(self.items) == 0:
            print("EMPTY STACK")
            return
        else:
            print("stack state before is ", self.items)
            del(self.items[-1])
            print("new stack state is", self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            print ("EMPTY STACK")
        else:
            print("stack not empty")


# LIST
# First in First out
# Using list, dequeue element at index 0
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getContents(self):
        return self.data

    def __repr__(self):
        return str(self.data)

    # def __str__(self):
    #     return str(self.data)

def print_list(node):
    while node is not None:
        print(node.getContents())
        node = node.next
    print()

# Adding a new node to the beginning of the list
def add(node, newdata):
    newNode = Node(newdata)
    newNode.next = node
    return newNode

def addAfter(headNode, midNode, newdata):
    newNode = Node(newdata)
    found = False
    pointNode = headNode
    if headNode is None:
        return newNode
    if midNode is None:
        return None
    while not found and pointNode is not None:
        if pointNode == midNode:
            newNode.next = pointNode.next
            pointNode.next = newNode
            found = True
        else:
            pointNode = pointNode.next
    return headNode


def delete(headNode, delNode):
    # When given only the element to delete, use of 2 pointers
    # is required. one at the head and the other at the second element
    if headNode is None or delNode is None:
        return None
    pointNode = headNode
    if delNode == headNode:
        headNode = headNode.next
        return headNode
    deleted = False
    while pointNode is not None:
        if pointNode.next == delNode:
            pointNode.next = delNode.next
            deleted = True
            break
        else:
            pointNode = pointNode.next
    if not deleted:
        print("ELEMENT TO DELETE NOT FOUND")
    return headNode






if __name__ == "__main__":
    node1 = Node('car')
    node2 = Node("bus")
    node3 = Node("lorry")
    node1.next = node2
    node2.next = node3
    print("ORIGINAL LIST")
    print_list(node1)
    print("ADDING TRUCK TO HEAD OF LIST")
    newHead = add(node1, "truck")
    print_list(newHead)
    print("ADDING BIKE TO MIDDLE OF LIST")
    newList=addAfter(newHead,node2, "bike")
    print_list(newList)
    print("DELETING HEAD ELEMENT")
    afterdelete = delete(newHead, newHead)
    print_list(afterdelete)
    print("DELETING MIDDLE ELEMENT")
    afterdelete2 = delete(afterdelete, node2.next)
    print_list(afterdelete2)

    # myStack = UseStack()
    # myStack.push(2)
    # myStack.push(5)
    # myStack.isEmpty()
    # myStack.pop()
    # myStack.pop()
    # myStack.isEmpty()
    # myStack.pop()