# Instances of Node class will be created in LinkedList below
# e.g. When adding a new entry in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def count(self):
        if self.head == None:
            return 0
        else:
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.next

            return count

    def addToHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addToTail(self, data):
        node = Node(data)
        node.next = None

        # Best case, if current head is None (List empty) -> time complexity Θ(1)
        if self.head is None:
            self.head = node

        # All other cases, we have to traverse the entire array -> time complexity Θ(n)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def access(self, position):
        current = self.head

        while position > 1 and current.next is not None:
            current = current.next
            position -= 1

        if position == 1:
            return current  # item at position is accessible and found.
        else:
            return -1  # item not accessible (Out of bound).

    def search(self, data):
        current = self.head

        while current.data is not None:
            if current.data == data:
                return current
            else:
                current = current.next
        return -1

    def insertInto(self, data, position):
        if position == 1:  # front of list
            self.addToHead(data)
        elif position > self.count():  # end of list
            self.addToTail(data)
        else:  # in between first and last node
            before_node = self.access(position - 1)
            after_node = before_node.next
            node = Node(data)
            before_node.next = node
            node.next = after_node

    def delete(self, position):
        if position == 1:  # front of list
            next_node = self.head.next
            self.head = next_node

        elif position > 1 and self.count() >= position:  # between first and last node
            before_node = self.access(position - 1)
            after_node = before_node.next.next
            before_node.next = after_node

        else:
            return -1

    def reverse(self):
        pass
        # current = self.head
        # next = current.next
        # current.next = None  # set up first element to become last

        # while next is not None:
        #     next.next = current
        #     current = next
        #     next = current.next

        # self.head = current  # set up last element to become first


list = LinkedList()
list.addToHead(10)
list.addToHead(20)
list.addToHead(30)
list.addToTail(30)
