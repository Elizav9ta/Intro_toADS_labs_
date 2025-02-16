class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())  
values = list(map(int, input().split()))  

# Build linked list
head = ListNode(values[0])  
current = head  
for val in values[1:]:  
    current.next = ListNode(val)  
    current = current.next  

current = head  
while current and current.next:  
    current.next = current.next.next  
    current = current.next  


current = head  
while current:  
    print(current.val, end=" ")  
    current = current.next  
