word = "error"
with open("error.txt", "r") as file:
    for line in file:
        if word in line:
            print(line.strip())