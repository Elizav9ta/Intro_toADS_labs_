class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMaxSum(head):
    max_sum = float('-inf')
    current_sum = 0

    while head:
        current_sum += head.val
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
        
        head = head.next

    return max_sum

# Читаем ввод
n = int(input())  # Число элементов
values = list(map(int, input().split()))  # Значения списка

# Создаём связанный список
head = ListNode(values[0])
current = head
for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

# Вызываем функцию и печатаем результат
print(findMaxSum(head))
