class Node():

    def __init__(self, data, next, prev):
        self.data = data
        self.next_node = next
        self.previous_node = prev

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self):
        self.head = None


    def add_to_list(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next_node = self.head
            #self.head.previous_node = node
            node.next_node.previous_node = node
            self.head = node


    def __repr__(self):
        if self.head == None:
            print "EMPTY LIST"
            return None
        top = self.head
        lis = ""
        while top is not None:
            lis += str(top.data)
            top = top.next_node
        return lis

    # changes the direction of the arrwos and reverses next and previous nodes
    # for each node
    # you should set the last prev to be the head node after the while loop is done
    #YOU ALWAYS HAVE TO RESET THE HEADFOR
    def reverse(self):
        if self.head is None:
            return None
        prev = None
        current = self.head
        while current is not None:
            next_to_do = current.next_node
            current.next_node = prev
            prev = current
            current = next_to_do
        self.head = prev



    # call the recursive function if head is not none
    def reverse2(self):
        if self.head is None:
            return
        self.recursive_reverse(self.head, None)

    # function takes a current node and its previous node
    # if the current node was the last, it sets it as head
    # else it gets the next node to work on,
    # sets the curr_node's next node to be its previous node
    # and then call itself with the next node it got and the current node(as previous of the next node it got)
    # ITS THE SAME AS THE ITERATIVE REALLY!
    def recursive_reverse(self, curr, prev):
        if curr.next_node is None:
            self.head = curr
            curr.next_node = prev
            return
        next_to_do = curr.next_node
        curr.next_node = prev
        self.recursive_reverse(next_to_do, curr)




#NOTE::: Whenever you do something at the head or tail,
# always reset the head or tail
def main():
    my_list = LinkedList()
    for i in range(5):
        new_node = Node(i, None, None)
        my_list.add_to_list(new_node)
    print my_list
    my_list.reverse()
    print "iterative reverse", my_list
    my_list2 = LinkedList()
    for i in range(5,10):
        new_node = Node(i, None, None)
        my_list2.add_to_list(new_node)
    print my_list2
    my_list2.reverse2()
    print "recursive reverse", my_list2



main()