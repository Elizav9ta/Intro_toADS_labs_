class Node:
    def __init__(self, book):
        self.book = book
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, book):
        new_node = Node(book)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("ok")

    def add_back(self, book):
        new_node = Node(book)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print("ok")

    def erase_front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.book)
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # Если список стал пустым

    def erase_back(self):
        if self.tail is None:
            print("error")
        else:
            print(self.tail.book)
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None  # Если список стал пустым

    def front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.book)

    def back(self):
        if self.tail is None:
            print("error")
        else:
            print(self.tail.book)

    def clear(self):
        self.head = self.tail = None
        print("ok")

def main():
    dll = DoublyLinkedList()
    while True:
        command = input().split(maxsplit=1)
        if command[0] == "add_front":
            dll.add_front(command[1])
        elif command[0] == "add_back":
            dll.add_back(command[1])
        elif command[0] == "erase_front":
            dll.erase_front()
        elif command[0] == "erase_back":
            dll.erase_back()
        elif command[0] == "front":
            dll.front()
        elif command[0] == "back":
            dll.back()
        elif command[0] == "clear":
            dll.clear()
        elif command[0] == "exit":
            print("goodbye")
            break

if __name__ == "__main__":
    main()
