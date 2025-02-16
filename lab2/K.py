from collections import deque, defaultdict

def first_non_repeating(stream):
    queue = deque()
    freq = defaultdict(int)
    result = []

    for char in stream:
        queue.append(char)
        freq[char] += 1
        
        while queue and freq[queue[0]] > 1:
            queue.popleft()
        
        result.append(queue[0] if queue else "-1")

    return " ".join(result)

def main():
    T = int(input())  # Количество тестов
    for _ in range(T):
        N = int(input())  # Размер потока
        stream = input().split()  # Символы потока
        print(first_non_repeating(stream))

if __name__ == "__main__":
    main()
