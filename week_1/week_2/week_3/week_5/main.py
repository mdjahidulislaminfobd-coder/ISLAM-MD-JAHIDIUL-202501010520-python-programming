from utils import calculate_total, print_receipt

name = input("Enter customer name: ")

coffee = int(input("Enter coffee quantity: "))
tea = int(input("Enter tea quantity: "))
sandwich = int(input("Enter sandwich quantity: "))

total = calculate_total(coffee, tea, sandwich)

print_receipt(name, coffee, tea, sandwich, total)