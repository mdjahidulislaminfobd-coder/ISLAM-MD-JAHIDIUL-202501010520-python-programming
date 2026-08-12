def check_computers():

    computers = []

    for number in range(1, 6):

        status = input(f"Computer {number} Status (A/U/M): ").upper()

        computers.append(status)

    return computers