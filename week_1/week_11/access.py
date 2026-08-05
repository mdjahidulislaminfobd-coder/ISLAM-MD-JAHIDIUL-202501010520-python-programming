# access.py

def check_access(is_registered, is_lab_open, is_computer_available):
    """
    Checks conditions and returns True for 'Access Granted' 
    or False for 'Access Denied'.
    """
    if is_registered == 'Y' and is_lab_open == 'Y' and is_computer_available == 'Y':
        return True
    else:
        return False

def get_reason(is_registered, is_lab_open, is_computer_available):
    """
    Returns the specific reason why access was denied or granted.
    """
    if is_registered != 'Y':
        return "Student is not registered"
    elif is_lab_open != 'Y':
        return "Computer lab is closed"
    elif is_computer_available != 'Y':
        return "No available computer"
    else:
        return "Welcome to the lab."