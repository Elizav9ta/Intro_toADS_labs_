import sys
import bisect

def solve():
    # Читаем количество противников
    N = int(sys.stdin.readline())
    
    # Читаем их силы и сортируем
    competitors = list(map(int, sys.stdin.readline().split()))
    competitors.sort()
    
    # Префиксная сумма для быстрой суммы сил
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + competitors[i]

    # Читаем количество раундов
    Q = int(sys.stdin.readline())

    # Обрабатываем каждый раунд
    results = []
    for _ in range(Q):
        P = int(sys.stdin.readline())
        
        # Найти количество побеждённых (бинарный поиск)
        idx = bisect.bisect_right(competitors, P)
        
        # Количество побеждённых и их сумма
        count = idx
        total_power = prefix_sum[idx]
        
        # Сохраняем результат
        results.append(f"{count} {total_power}")
    
    # Вывод всех результатов за один раз (ускоряет выполнение)
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
