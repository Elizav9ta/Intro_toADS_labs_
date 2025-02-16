import sys

def can_cover(S, pastures, K):
    """ Проверяет, покрывает ли квадрат со стороной S хотя бы K пастбищ """
    count = sum(1 for x1, y1, x2, y2 in pastures if x2 <= S and y2 <= S)
    return count >= K

def min_square_size(N, K, pastures):
    """ Бинарный поиск минимального S, чтобы покрыть хотя бы K пастбищ """
    # Кандидаты для S — max(x2, y2) из всех пастбищ
    candidates = sorted(set(max(x2, y2) for _, _, x2, y2 in pastures))
    
    # Бинарный поиск по кандидатам
    left, right = 0, len(candidates) - 1
    while left < right:
        mid = (left + right) // 2
        if can_cover(candidates[mid], pastures, K):
            right = mid  # Пробуем уменьшить S
        else:
            left = mid + 1  # Увеличиваем S
    
    return candidates[left]

def main():

    N, K = map(int, sys.stdin.readline().split())
    pastures = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    print(min_square_size(N, K, pastures))

if __name__ == "__main__":
    main()
