def count_available(computers):

    available = 0

    for status in computers:

        if status == "A":
            available += 1

    return available