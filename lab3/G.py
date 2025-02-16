import sys
import math

def can_deliver_with_capacity(A, N, F, capacity):
    """Проверяет, можно ли доставить все подарки за F рейсов при данном C"""
    flights_needed = sum(math.ceil(a / capacity) for a in A)
    return flights_needed <= F

def find_min_capacity(N, F, A):
    """Бинарный поиск по ответу для минимальной вместимости мешка"""
    left, right = 1, max(A)
    while left < right:
        mid = (left + right) // 2
        if can_deliver_with_capacity(A, N, F, mid):
            right = mid  # Ищем ещё меньшее C
        else:
            left = mid + 1  # Увеличиваем C, так как не укладываемся в F рейсов
    return left

def solve():
    # Читаем входные данные
    N, F = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Вычисляем минимальную вместимость мешка
    print(find_min_capacity(N, F, A))

if __name__ == "__main__":
    solve()
