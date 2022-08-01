class LinkedList:
    def __init__(self):
        self.head = None

    def push_in_front(self, data):
        if self.head is None:
            self.head = Stack(data)
        else:
            first = Stack(data)
            first.next = self.head
            self.head = first

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

class Stack:

    def __init__(self, data):
        self.data = data
        self.next = None

new = LinkedList()
new.push_in_front(1)
new.push_in_front(2)
new.push_in_front(3)
new.push_in_front(4)