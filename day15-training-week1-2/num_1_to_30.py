new_list = []

for i in range(1, 31):
    if i % 4 == 0 and i % 6 != 0:
        new_list.append(i)

print(f"Result: {new_list}")