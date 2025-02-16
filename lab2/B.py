class ListNode:
    def __init__(self, val=""):
        self.val = val
        self.next = None

def shift_linked_list(head, k, n):
    if not head or k == 0 or k % n == 0:
        return head  # Если сдвиг не требуется

    k = k % n  # Убираем лишние полные циклы
    current = head

    # Находим (k-1)-й узел
    for _ in range(k - 1):
        current = current.next

    # Новый head - следующий за current узел
    new_head = current.next
    current.next = None  # Разрываем связь

    # Идём до конца нового списка, чтобы соединить с началом
    last = new_head
    while last.next:
        last = last.next
    last.next = head  # Переносим старую голову в конец

    return new_head

def build_linked_list(words):
    if not words:
        return None
    head = ListNode(words[0])
    current = head
    for word in words[1:]:
        current.next = ListNode(word)
        current = current.next
    return head

def print_linked_list(head):
    words = []
    while head:
        words.append(head.val)
        head = head.next
    print(" ".join(words))

n, k = map(int, input().split())
words = input().split()

head = build_linked_list(words)

new_head = shift_linked_list(head, k, n)

print_linked_list(new_head)
