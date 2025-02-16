def find_coordinates(t, targets, n, m, matrix):
    positions = {}  # Словарь для хранения координат чисел в змейке
    
    for i in range(n):
        row = matrix[i]
        if i % 2 == 0:
            for j in range(m):
                positions[row[j]] = (i, j)
        else:
            for j in range(m):
                positions[row[j]] = (i, j)

    for num in targets:
        if num in positions:
            print(*positions[num])
        else:
            print(-1)

t = int(input())  # Количество искомых элементов
targets = list(map(int, input().split()))  # Искомые элементы

n, m = map(int, input().split())  # Размеры матрицы

matrix = []  
for _ in range(n):
    matrix.append(list(map(int, input().split())))

find_coordinates(t, targets, n, m, matrix)
