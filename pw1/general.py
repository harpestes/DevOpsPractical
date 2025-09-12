def print_product_names(product_names, index=0):
    if index < len(product_names):
        print(product_names[index])
        print_product_names(product_names, index + 1)

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