def input_product():
    products = {}
    while True:
        name = input("Enter product name or 'stop' to exit: ")
        if name.lower() == 'stop':
            break
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock on warehouse: "))
        products[name] = {'Prise': price, 'Stock': stock}

    return products

products = input_product()
print(products)

def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Stock'] * details['Prise']
        print(f"Вартість залишку для {product}: {stock_value}")

calculate_stock_value(products)
