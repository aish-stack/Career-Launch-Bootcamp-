
Project · PY
"""
Mini Project: Simple Student Grade Calculator
Author: Prathamesh J. Warade
"""
 
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"
 
def main():
    name = input("Enter student name: ")
    marks = float(input("Enter marks (out of 100): "))
    print(f"{name}'s Grade: {grade(marks)}")
 
if __name__ == "__main__":
    main()
 
