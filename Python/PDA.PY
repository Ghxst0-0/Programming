while True:
    name= (input("what's your name?"))
    reg_no = (input("Please enter your registration number: "))
    while True:
        marks= []
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

        if len(marks) == 0:
            print("No marks entered. Please enter at least one mark.")
            continue
        print(" Hello", name, " registration number", reg_no, "your marks are", marks, ". Please confirm if details are correct.")
        break
    confirmation=input("Type 'yes' to confirm or 'no' to re-enter your details: ")
    if confirmation == "yes":
        total = sum(marks)
        mean = sum(marks) / len(marks)
        print("Your total marks are:", total)
        print("Your mean marks are:", mean)
        break
    elif confirmation == "no":
        print("Please re-enter your details.")
        continue
    else:
        print("Invalid input. Please type 'yes' or 'no'.")






