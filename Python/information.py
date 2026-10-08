
def get_student_name():
    name = input("What's your name? ")
    return name

def get_student_reg_no():
    reg_no = input("Please enter your registration number: ")
    return reg_no

def get_student_marks():
    marks = []
    while True:
        mark = input("Enter your marks (or type 'done' to finish): ")
        if mark.lower() == 'done':
            break
        try:
            mark = float(mark)
            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100. Please re-enter your marks.")
                continue
            marks.append(mark)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
    return marks

def get_confirmed_marks():
    student_marks = get_student_marks()
    while not student_marks:
        print("No marks entered. Please enter at least one mark.")
        student_marks = get_student_marks()
    return student_marks

def confirm_details():
        while True:
            print("Are your details correct?")
            confirmation = input("Type 'yes' to confirm or 'no' to re-enter your details: ")
            if confirmation.lower() == 'no':
                return False
            elif confirmation.lower() != 'yes':
                print("Invalid input. Please type 'yes' or 'no'.")
                continue
            else:
                print("Details confirmed.")
                return True
