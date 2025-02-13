def process_string(s):
    stack = []
    for char in s:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def are_strings_equal(s1, s2):
    return process_string(s1) == process_string(s2)

s1, s2 = input().split()
print("Yes" if are_strings_equal(s1, s2) else "No")
