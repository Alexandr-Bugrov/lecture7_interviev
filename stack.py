class Stack:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.list_length = 0

    def push_back(self, data):
        if self.head is None:
            self.head = Stack(data)
        else:
            first = Stack(data)
            first.next = self.head
            self.head = first
        self.list_length += 1

    def push_front(self, data):
        if self.head is None:
            self.head = Stack(data)
        else:
            end = Stack(data)
            obj = self.head
            while obj.next:
                obj = obj.next
            obj.next = end
        self.list_length += 1

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def pop(self):
        obj = self.head
        if obj.next is None:
            self.head = None
            self.list_length = 0
        else:
            while obj.next.next is not None:
                obj = obj.next
            obj.next = None
            self.list_length -= 1

    def peek(self):
        obj = self.head
        while obj.next:
            obj = obj.next
        return obj

    def size(self):
        return self.list_length


new = LinkedList()
new.push_front(1)
new.push_front(3)
new.push_front(4)
new.pop()
print(new.size())
print(new.peek())