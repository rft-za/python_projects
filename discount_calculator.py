def calculate_discount(price, discount):
    final_discount = price - (price * (discount / 100))
    return final_discount

while True:
    try:
        print("*****DISCOUNT_CALCULATOR*****")
        input_price = float(input("Enter price(¥): "))
        if input_price <= 0:
            print("Price should be greater than 0.")
            print()
        else:
            break
    except ValueError:
        print("Price should be an integer.")

while True:
    try:
        input_discount = float(input("Enter discount(%): "))
        if not (0 <= input_discount <= 100):
            print("Discount should be between 0 and 100.")
            print()
        else:
            break
    except ValueError:
        print("Discount should be an integer.")

print(f"Final price: ¥{calculate_discount(input_price, input_discount)}")
print("*****************************")
