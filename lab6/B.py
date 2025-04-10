from collections import Counter

def find_common_numbers(n, m, list1, list2):
    count1 = Counter(list1)  # Count  in first list
    count2 = Counter(list2)  # Count  in second list

    common_elements = []
    
    for num in sorted(count1.keys() & count2.keys()):  # Find intersection keys
        common_elements.extend([num] * min(count1[num], count2[num]))  # Keep min occurrences
    
    print(" ".join(map(str, common_elements)))

n, m = map(int, input().split())

list1 = list(map(int, input().split())) if n > 0 else []
list2 = list(map(int, input().split())) if m > 0 else []

find_common_numbers(n, m, list1, list2)
