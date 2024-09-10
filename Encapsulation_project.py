class Student:
    def __init__(self,name,roll_number):
        self._name = name
        self._roll_number = roll_number
        self._grades = {}
        self._attendance = 0

#Adds or updates the grade for a subject.
    def add_grade(self,subject,grade):
        self._grades[subject] = grade

#Returns the grade for a specific subject
    def get_grade(self,subject):
        return f"{subject}: {self._grades.get(subject)} Marks"

#Calculates and returns the student's average grade across all subjects.
    def get_average_grade(self):
        all_marks = []
        for mark in self._grades.values():
            all_marks.append(mark)

        total_marks = 0
        for m in all_marks:
            total_marks += m
        return round(total_marks/len(all_marks),2)
       
# Increments the student's attendance by 1.
    def mark_attendance(self):
        self._attendance += 1

#Returns the number of days the student has attended.
    def get_attendance(self):
        return f"Total days present: {self._attendance}"

#Returns a summary of the student’s details (name, roll number, grades, and attendance).
    def get_student_info(self):
        return f"Student_Name: {self._name}\nRoll_No: {self._roll_number}\nMarks: {self._grades}\nGrade: {Student.get_average_grade(self)}\nAttendance: {self._attendance}"

#!StudentManager class that can manage multiple students.
class StudentManager:
    def __init__(self):
        self._students = {}

# Adds a new student to the system.
    def add_student(self,student):
        if student._roll_number in self._students:
            print(f"Student with Roll Number {student._roll_number} already exists.")
        else:
            self._students[student._roll_number] = student   

#Removes a student by roll number.
    def remove_student(self,roll_number):
        if roll_number in self._students:
            removed_student = self._students.pop(roll_number)
            print(f"Student {removed_student._name} removed.")
        else:
            print('no student found')

#Returns the Student object for the given roll number
    def get_student(self,roll_number):
        return self._students.get(roll_number,None)

#Lists all students in the system with their details.
    def list_all_student(self):
        if not self._students:
            print('No student in the system')
        else:
            for roll_number,student in self._students.items():
                print(student.get_student_info())
                print('------------')




manager = StudentManager()

std1 = Student("Chethan",22)
std2 = Student("Santhosh",25)
std3 = Student('Prem',30)

manager.add_student(std1)
manager.add_student(std2)
manager.add_student(std3)


std1.add_grade('Telugu',92)
std1.add_grade('Hindi',83)
std1.add_grade('English',90)
std2.add_grade('Telugu',90)
std2.add_grade('Hindi',81)
std2.add_grade('English',89)
std3.add_grade('Telugu',87)
std3.add_grade('Hindi',89)
std3.add_grade('English',85)


std1.mark_attendance()
std1.mark_attendance()
std1.mark_attendance()
std1.mark_attendance()
std1.mark_attendance()
std2.mark_attendance()
std2.mark_attendance()
std2.mark_attendance()
std3.mark_attendance()
std3.mark_attendance()
std3.mark_attendance()

print(std1.get_average_grade())
print(std2.get_average_grade())
print(std3.get_average_grade())

manager.list_all_student()