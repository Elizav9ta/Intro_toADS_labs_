def track_nickname_changes(n, changes):
    nickname_map = {}  

    for old, new in changes:
        if old in nickname_map:
            original = nickname_map[old]
            del nickname_map[old]  
        else:
            original = old
        
        nickname_map[new] = original

    result = sorted((original, final) for final, original in nickname_map.items())

    print(len(result))
    for original, final in result:
        print(original, final)

n = int(input())
changes = [input().split() for _ in range(n)]

track_nickname_changes(n, changes)
