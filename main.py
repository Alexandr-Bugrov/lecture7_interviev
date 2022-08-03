from stack import LinkedList

if __name__ == '__main__':
    new = LinkedList()
    string = '[([])((([[[]]])))]{()}'
    new.push_end(string)
    print(new.filter())