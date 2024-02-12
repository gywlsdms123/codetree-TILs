a, b = map(int, input().split())

if a > b:
    for _ in range(a, b-1, -1):
        print(_, end=" ")
elif a < b:
    for _ in range(b, a-1, -1):
        print(_, end=" ")