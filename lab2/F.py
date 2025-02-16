class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, data, position):
    new_node = ListNode(data)

    # If inserting at head (position 0)
    if position == 0:
        new_node.next = head
        return new_node  # New head of the list

    current = head
    for _ in range(position - 1):
        if current is None:
            return head  # If position is out of bounds, do nothing
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

n = int(input())
if n > 0:
    head = ListNode(int(input()))
    current = head
    for _ in range(n - 1):
        current.next = ListNode(int(input()))
        current = current.next
else:
    head = None  # Handle case of an empty list

data = int(input())
position = int(input())

head = insert_node(head, data, position)

current = head
while current:
    print(current.val, end=" ")
    current = current.next
