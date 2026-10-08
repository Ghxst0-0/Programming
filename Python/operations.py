def calculate_total(marks):
    total = sum(marks)
    return total

def calculate_mean(marks):
    n = len(marks)
    if n == 0:
        return 0
    mean = calculate_total(marks) / n
    return mean

def find_highest_lowest(marks):
    n = len(marks)
    if n == 0:
        return None, None
    highest = max(marks)
    lowest = min(marks)
    return highest, lowest

def calculate_median(marks):
    n = len(marks)
    if n == 0:
        return None

    sorted_marks = sorted(marks)
    mid = n // 2

    if n % 2 == 0:
        median = (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        median = sorted_marks[mid]

    return median

if __name__ == "__main__":

    print("operations.py has been loaded")
