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

    def filter(self):
        if self.size() % 2 != 0:
            return 'Несбалансированно'
            pass
        obj = self.head
        while obj.next:
            if obj.data == '(' and obj.next.data in ']}':
                return 'Несбалансированно'
            elif obj.data == '[' and obj.next.data in ')}':
                return 'Несбалансированно'
            elif obj.data == '{' and obj.next.data in ')]':
                return 'Несбалансированно'
            obj = obj.next

    def brackets_counter(self):
        obj = self.head
        square_brackets = 0
        curly_brackets = 0
        round_brackets = 0
        i = False
        while obj.next:
            if i is True:
                obj = obj.next
            i = True
            if obj.data == '(':
                round_brackets += 1
            elif obj.data == ')':
                round_brackets -= 1
            elif obj.data == '[':
                square_brackets += 1
            elif obj.data == ']':
                square_brackets -= 1
            elif obj.data == '{':
                curly_brackets += 1
            elif obj.data == '}':
                curly_brackets -= 1
        if square_brackets != 0 or curly_brackets != 0 or round_brackets != 0:
            return 'Несбалансированно'
        else:
            return 'Cбалансированно'

    def checking(self):
        filter_result = self.filter()
        if filter_result is None:
            print(self.brackets_counter())
        else:
            print(filter_result)


new = LinkedList()
string = '[([])((([[[]]])))]{()}'
new.filler(string)
new.checking()

