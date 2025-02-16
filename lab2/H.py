class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x, p):
        new_node = Node(x)
        if p == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(p - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return self.head

    def remove(self, p):
        if p == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(p - 1):
                current = current.next
            current.next = current.next.next
        return self.head

    def print_list(self):
        if not self.head:
            print(-1)
        else:
            current = self.head
            values = []
            while current:
                values.append(str(current.val))
                current = current.next
            print(" ".join(values))

    def replace(self, p1, p2):
        if p1 == p2:
            return self.head
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        # Removing the node at p1
        node_to_move = nodes.pop(p1)
        # Inserting it at p2
        nodes.insert(p2, node_to_move)
        # Rebuilding the list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        self.head = nodes[0]
        return self.head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head

    def cyclic_left(self, x):
        if not self.head or x == 0:
            return self.head
        # Get the length of the list
        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1
        # Make the list cyclic
        x = x % length  # In case x is greater than the list length
        if x == 0:
            return self.head
        current.next = self.head  # Connect the last node to head to form a loop
        new_tail = self.head
        for _ in range(x - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        return self.head

    def cyclic_right(self, x):
        if not self.head or x == 0:
            return self.head
        # Get the length of the list
        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1
        # Make the list cyclic
        x = x % length  # In case x is greater than the list length
        if x == 0:
            return self.head
        current.next = self.head  # Connect the last node to head to form a loop
        new_tail = self.head
        for _ in range(length - x - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        self.head = new_head
        return self.head

def main():
    linked_list = LinkedList()
    
    while True:
        command = list(map(int, input().split()))
        if command[0] == 0:
            break
        elif command[0] == 1:
            linked_list.insert(command[1], command[2])
        elif command[0] == 2:
            linked_list.remove(command[1])
        elif command[0] == 3:
            linked_list.print_list()
        elif command[0] == 4:
            linked_list.replace(command[1], command[2])
        elif command[0] == 5:
            linked_list.reverse()
        elif command[0] == 6:
            linked_list.cyclic_left(command[1])
        elif command[0] == 7:
            linked_list.cyclic_right(command[1])

if __name__ == "__main__":
    main()