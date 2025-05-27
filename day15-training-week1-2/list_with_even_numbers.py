numbers = [20, 41, 50, 43, 12, 34, 4, 7,
           8, 0, 15, 54, 34, 56, 123, 23,
           87, 99, 34, 54, 65, 68, 123, 988, 23, 56]

even_sum = 0

for i in numbers:
    if i % 2 == 0:
        even_sum += i

print(even_sum)