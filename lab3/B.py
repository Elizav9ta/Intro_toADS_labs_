def can_partition(arr, n, k, max_sum):
    count = 1  # Количество блоков
    current_sum = 0

    for num in arr:
        if current_sum + num > max_sum:
            count += 1
            current_sum = num  # Начинаем новый блок
        else:
            current_sum += num
        
        if count > k:
            return False  # Превысили допустимое число блоков

    return True  


def find_min_max_ghouls(n, k, arr):
    left, right = max(arr), sum(arr)  # Границы бинарного поиска
    answer = right

    while left <= right:
        mid = (left + right) // 2  # Пробуем текущий максимум

        if can_partition(arr, n, k, mid):
            answer = mid  # Нашли более оптимальный максимум
            right = mid - 1  # Ищем меньший максимум
        else:
            left = mid + 1  # Увеличиваем возможный максимум

    return answer


n, k = map(int, input().split())  
arr = list(map(int, input().split())) 

print(find_min_max_ghouls(n, k, arr))
