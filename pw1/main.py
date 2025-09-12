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

products = input_product()
print(products)

def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Stock'] * details['Price']
        print(f"Stock value for {product}: {stock_value}")

calculate_stock_value(products)

def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Stock'] < 10:
            discount = details['Price'] * 0.05  # 5% знижка
            print(f"Discount for {product}: {discount} ({details['Price']} - 5%)")
            print(f"Total price for {product}: {details['Price'] - discount}")
        else:
            print(f"For {product} discount not applied, because stock is {details['Stock']} items.")

calculate_discount(products)

def print_product_names(product_names, index=0):
    if index < len(product_names):
        print(product_names[index])
        print_product_names(product_names, index + 1)


product_names = list(products.keys())
print_product_names(product_names)

def find_product_by_name(products, product_name, index=0):
    product_keys = list(products.keys())

    if index >= len(product_keys):
        print("Product not found.")
        return

    if product_keys[index] == product_name:
        product_info = products[product_name]
        print(f"Product found: Price - {product_info['Price']}, Stock - {product_info['Stock']}")
        return

    find_product_by_name(products, product_name, index + 1)

find_product_by_name(products, str(input("Enter product name to find: ")))
