def input_product():
    products = {}
    while True:
        name = input("Enter product name or 'stop' to exit: ")
        if name.lower() == 'stop':
            break
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock on warehouse: "))
        products[name] = {'Price': price, 'Stock': stock}

    return products