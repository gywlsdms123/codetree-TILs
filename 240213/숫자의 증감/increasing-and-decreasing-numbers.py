arr = input().split()

c, n = arr[0], int(arr[1])

if c == 'A':
    for _ in range(1, n+1):
        print(_, end=' ')
elif c == 'D':
    for _ in range(n, 0, -1):
        print(_, end=' ')