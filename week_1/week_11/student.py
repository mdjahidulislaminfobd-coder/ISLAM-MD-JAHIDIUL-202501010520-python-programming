# student.py

def get_student():
    print("===== Computer Lab Access =====")
    
    # Prompt user inputs
    name = input("Student Name : ")
    student_id = input("Student ID : ")
    
    # Prompt conditions as 'Y' or 'N'
    is_registered = input("Registered for today's lab? (Y/N): ").upper()
    is_lab_open = input("Is the lab currently open? (Y/N): ").upper()
    is_computer_available = input("Computer Available? (Y/N): ").upper()
    
    # Return all values as a tuple
    return name, student_id, is_registered, is_lab_open, is_computer_available