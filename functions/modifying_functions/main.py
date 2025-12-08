def apply_discount(price, discount=0.05):
    discounted = price * (1-discount)
    return discounted


def apply_tax(price, tax=0.07):
    taxed = price * (1+tax)
    return taxed


def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, tax)
    return total_price

default = calculate_total (120)
print (f"Total cost with default discount and tax: ${default}")

custom = calculate_total (100, 0.1, 0.08)
print (f"Total cost with custom discount and tax: ${custom}")