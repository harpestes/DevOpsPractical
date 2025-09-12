def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Stock'] * details['Price']
        print(f"Stock value for {product}: {stock_value}")

def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Stock'] < 10:
            discount = details['Price'] * 0.05  # 5% знижка
            print(f"Discount for {product}: {discount} ({details['Price']} - 5%)")
            print(f"Total price for {product}: {details['Price'] - discount}")
        else:
            print(f"For {product} discount not applied, because stock is {details['Stock']} items.")