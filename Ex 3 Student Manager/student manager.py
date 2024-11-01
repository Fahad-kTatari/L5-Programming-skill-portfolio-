import tkinter as tk
from tkinter import messagebox, simpledialog

def load_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        num_students = int(file.readline().strip())
        for line in file:
            data = line.strip().split(',')
            student_number = int(data[0])
            student_name = data[1]
            coursework_marks = list(map(int, data[2:5]))
            exam_mark = int(data[5])
            total_coursework = sum(coursework_marks)
            overall_total = total_coursework + exam_mark
            percentage = (overall_total / 160) * 100
            students.append({
                'number': student_number,
                'name': student_name,
                'coursework': total_coursework,
                'exam': exam_mark,
                'percentage': percentage,
                'grade': calculate_grade(percentage)
            })
    return students

def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def display_student_record(student):
    window = tk.Toplevel()
    window.title("Student Record")
    tk.Label(window, text=f"Student Name: {student['name']}").pack()
    tk.Label(window, text=f"Student Number: {student['number']}").pack()
    tk.Label(window, text=f"Total Coursework Marks: {student['coursework']} / 60").pack()
    tk.Label(window, text=f"Exam Mark: {student['exam']} / 100").pack()
    tk.Label(window, text=f"Overall Percentage: {student['percentage']:.2f}%").pack()
    tk.Label(window, text=f"Grade: {student['grade']}").pack()
    tk.Button(window, text="Close", command=window.destroy).pack()

def view_all_students(students):
    for student in students:
        display_student_record(student)
    average_percentage = sum(s['percentage'] for s in students) / len(students)
    window = tk.Toplevel()
    window.title("Summary")
    tk.Label(window, text=f"Number of students: {len(students)}").pack()
    tk.Label(window, text=f"Average percentage: {average_percentage:.2f}%").pack()
    tk.Button(window, text="Close", command=window.destroy).pack()

def view_individual_student(students):
    search_term = simpledialog.askstring("Search Student", "Enter student name or student number:")
    if search_term:
        found_students = [s for s in students if search_term.lower() in s['name'].lower() or search_term == str(s['number'])]
        if found_students:
            for student in found_students:
                display_student_record(student)
        else:
            messagebox.showinfo("Search Result", "No student found with that name or number.")

def show_highest_score(students):
    highest_student = max(students, key=lambda s: s['percentage'])
    display_student_record(highest_student)

def show_lowest_score(students):
    lowest_student = min(students, key=lambda s: s['percentage'])
    display_student_record(lowest_student)

def main():
    students = load_student_data('studentMarks.txt')

    root = tk.Tk()
    root.title("Student Management System")

    tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="View All Student Records", command=lambda: view_all_students(students)).pack(pady=5)
    tk.Button(root, text="View Individual Student Record", command=lambda: view_individual_student(students)).pack(pady=5)
    tk.Button(root, text="Show Student with Highest Score", command=lambda: show_highest_score(students)).pack(pady=5)
    tk.Button(root, text="Show Student with Lowest Score", command=lambda: show_lowest_score(students)).pack(pady=5)
    tk.Button(root, text="Quit", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
