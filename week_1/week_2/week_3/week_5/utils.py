def calculate_total(coffee, tea, sandwich):
    Total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)
    return Total

def print_receipt(name, coffee, tea, sandwich, total):
    print("\n==== RECEIPT ====")
    print("Customer :", name)
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)
    print("____________________")
    print("Total = RM", format(total, ".2f"))