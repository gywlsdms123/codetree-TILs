numbers = [int(input()) for _ in range(5)]

even_count = sum(1 for number in numbers if number % 2 == 0)

print(even_count)