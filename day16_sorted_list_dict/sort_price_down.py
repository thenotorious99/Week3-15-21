products = {"banana": 2, "apple": 1, "orange": 3}

new_products = sorted(products.items(), key= lambda item: item[1], reverse=True)
print(new_products)
