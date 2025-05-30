products = {"banana": 2, "apple": 1, "orange": 3}

products_sort = sorted(products.items(), key=lambda item: item[1])

print(products_sort)