def display_status(computers, available):

    print("\n========== LAB STATUS ==========")

    for number in range(1, 6):

        print(f"Computer {number}: {computers[number - 1]}")

    print("-------------------------------")
    print(f"Available Computers: {available}")
    print("===============================")