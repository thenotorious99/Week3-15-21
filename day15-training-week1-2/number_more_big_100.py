numbers = [20, 41, 50, 43, 12, 34, 4, 7,
           8, 0, 15, 54, 34, 56, 123, 23,
           87, 99, 34, 54, 65, 68, 123, 988, 23, 56]

#Broqch
count = 0

# Obhojdane na vsichki chisla
for i in numbers:
    if i >= 100:
        count += 1

print(count)