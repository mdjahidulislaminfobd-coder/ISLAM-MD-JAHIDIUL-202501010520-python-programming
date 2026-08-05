# main.py

from student import get_student
from access import check_access, get_reason
from display import print_result

def main():
    # 1. Get student input
    name, student_id, is_registered, is_lab_open, is_computer_available = get_student()
    
    # 2. Determine access status
    is_granted = check_access(is_registered, is_lab_open, is_computer_available)
    
    if is_granted:
        status = "Access Granted"
    else:
        status = "Access Denied"
        
    # 3. Get the corresponding reason
    reason = get_reason(is_registered, is_lab_open, is_computer_available)
    
    # 4. Display the results
    print_result(name, student_id, status, reason)

if __name__ == "__main__":
    main()