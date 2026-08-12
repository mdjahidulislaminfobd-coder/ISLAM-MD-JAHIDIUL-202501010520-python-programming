from check_computers import check_computers
from count_available import count_available
from display_status import display_status


while True:

    computers = check_computers()

    available = count_available(computers)

    display_status(computers, available)

    choice = input("\nPerform another monitoring cycle? (Y/N): ").upper()

    if choice == "N":
        print("Monitoring stopped.")
        break