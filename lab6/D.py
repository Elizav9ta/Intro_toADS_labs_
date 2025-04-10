def sort_dates(n, dates):
    parsed_dates = [(d, int(d[6:]), int(d[3:5]), int(d[:2])) for d in dates]
    
    parsed_dates.sort(key=lambda x: (x[1], x[2], x[3]))

    for date in parsed_dates:
        print(date[0])

n = int(input())
dates = [input().strip() for _ in range(n)]

sort_dates(n, dates)
