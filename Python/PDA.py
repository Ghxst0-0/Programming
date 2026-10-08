import operations
import information
import output

def main():

    while True:
        student_name = information.get_student_name()
        student_reg_no = information.get_student_reg_no()
        student_marks = information.get_confirmed_marks()
        entries = len(student_marks)

        output.greet_student(student_name, student_reg_no, entries)
        confirmed = information.confirm_details()
        if not confirmed:
            continue

        result = operations.calculate_total(student_marks)
        output.display_total(result)
        mean = operations.calculate_mean(student_marks)
        output.display_mean(mean)
        highest, lowest = operations.find_highest_lowest(student_marks)
        output.display_highest_lowest(highest, lowest)
        median = operations.calculate_median(student_marks)
        output.display_median(median)

if __name__ == "__main__":
    main()
