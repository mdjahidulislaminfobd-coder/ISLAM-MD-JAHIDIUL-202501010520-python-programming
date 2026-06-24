# Student Average Calculator

# Ask user to enter the student's name
student_name = input("Enter Student Name: ")

# Ask user to enter Subject 1 mark and convert it to float
mark1 = float(input("Enter Subject 1 Mark: "))
# Ask user to enter Subject 2 mark and convert it to float
mark2 = float(input("Enter subject 2 Mark: "))
# Ask user to enter Subject 3 mark and convert it to floar
mark3 = float(input("Enter Subject 3 Mark: "))

# Calculate the total marks 
total = mark1 + mark2 + mark3 
# Calculate the average marks
average = total / 3

# Display a heading for the result section
print("/n----- Student Result -----")
# Display the student's name
print("Student Name:", student_name)
# Display the total marks
print("Total Marks:", total)
# Display the average marks
print("Average Marks:", average)

# Check whether the student passpes or fails
if average >= 50:
    # Display PASS is average is 50 or above 
    print("Status: PASS")
else:
    # Display FAIL is average is below 50
    print("Status: FAIL")