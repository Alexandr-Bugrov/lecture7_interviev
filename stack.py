class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.list_length = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            first = Node(data)
            first.next = self.head
            self.head = first
        self.list_length += 1

    def push_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            end = Node(data)
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
            while obj.next.next:
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

    def filler(self, your_string: str):
        for elem in your_string:
            self.push_end(elem)

    def filter(self, string:str):
        for data in string:
            if data in ['(', '[', '{']:
                self.push_end(data)
            elif data in [')', ']', '}'] and ((data == ')' and self.peek() == '(') or
                                              (data == ']' and self.peek() == '[') or (data == '}' and self.peek() == '{')):
                self.pop()
        if self.list_length == 0:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'


