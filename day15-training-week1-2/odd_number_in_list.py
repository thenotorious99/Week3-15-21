numbers = [20, 41, 50, 43, 12, 34, 4, 7,
           8, 0, 15, 54, 34, 56, 123, 23,
           87, 99, 34, 54, 65, 68, 123, 988, 23, 56]

odd_nums = [num for num in numbers if num % 2 != 0]

if odd_nums:
    max_odd = max(odd_nums)
    print(max_odd)

