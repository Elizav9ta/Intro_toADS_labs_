from collections import deque

def deque_operations(commands):
    dq = deque()
    
    for command in commands:
        op = command.split()
        
        if op[0] == '+':
            dq.appendleft(int(op[1]))
        elif op[0] == '-':
            dq.append(int(op[1]))
        elif op[0] == '*':
            if len(dq) == 0:
                print("error")
            else:
                first = dq.popleft()
                last = dq.pop() if dq else first  # Handle single element case
                print(first + last)
        elif op[0] == '!':
            break

commands = []
while True:
    try:
        line = input().strip()
        if line:
            commands.append(line)
        if line == '!':
            break
    except EOFError:
        break

deque_operations(commands)
