# Student Grade Predictor
# Author: Muhammad Ameen J.
# Description: Predicts student grade and performance category based on marks

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade(average):
    if average >= 90:
        return "O", "Outstanding"
    elif average >= 80:
        return "A+", "Excellent"
    elif average >= 70:
        return "A", "Very Good"
    elif average >= 60:
        return "B+", "Good"
    elif average >= 50:
        return "B", "Average"
    elif average >= 40:
        return "C", "Pass"
    else:
        return "F", "Fail"

def predict_grade():
    print("=" * 45)
    print("       STUDENT GRADE PREDICTOR")
    print("=" * 45)

    name = input("Enter student name: ")
    subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]

    marks_list = []
    print("\nEnter marks for each subject:")
    for subject in subjects:
        marks_list.append(get_marks(subject))

    total = sum(marks_list)
    average = total / len(subjects)
    grade, performance = calculate_grade(average)

    print("\n" + "=" * 45)
    print(f"  RESULT FOR: {name.upper()}")
    print("=" * 45)
    for i, subject in enumerate(subjects):
        print(f"  {subject:<25} : {marks_list[i]:.1f}")
    print("-" * 45)
    print(f"  Total Marks     : {total:.1f} / {len(subjects)*100}")
    print(f"  Average         : {average:.2f}%")
    print(f"  Grade           : {grade}")
    print(f"  Performance     : {performance}")
    print("=" * 45)

    if grade == "F":
        print("  Keep working hard! You can do it!")
    elif average >= 80:
        print("  Great job! Keep it up!")
    else:
        print("  Good effort! Aim higher next time!")
    print("=" * 45)

if __name__ == "__main__":
    predict_grade()
