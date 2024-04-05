students = {
    "Ali Yilmaz": {"Midterm": 85, "Final": 90, "Oral": 88},
    "Ayse Demir": {"Midterm": 75, "Final": 80, "Oral": 78},
    "Mehmet Kaya": {"Midterm": 90, "Final": 95, "Oral": 92},
    "Fatma Yildiz": {"Midterm": 70, "Final": 75, "Oral": 72},
    "Mustafa Arslan": {"Midterm": 80, "Final": 85, "Oral": 82},
    "Zeynep Celik": {"Midterm": 65, "Final": 70, "Oral": 68},
    "Ahmet Sahin": {"Midterm": 75, "Final": 80, "Oral": 78},
    "Aylin Kurt": {"Midterm": 85, "Final": 90, "Oral": 88},
    "Emre Tekin": {"Midterm": 80, "Final": 85, "Oral": 82},
    "Gizem Bulut": {"Midterm": 75, "Final": 80, "Oral": 78}
}
student_dict={}
for student, grades in students.items():
    midterm = grades["Midterm"]
    final = grades["Final"]
    oral = grades["Oral"]
    grades["GPA"] = (midterm + final + oral) / 3
    student_dict[student]= round(grades["GPA"],3)
print(student_dict)
  

highest_gpa_student = max(students, key=lambda x: students[x]["GPA"])
print("Student with the highest GPA:", highest_gpa_student)

names_list = [(name.split()[0], name.split()[1]) for name in students.keys()]

sorted_names = sorted(names_list)
print("Sorted list of names:")
for first_name, last_name in sorted_names:
    print(first_name, last_name)

low_gpa_students = {student for student, grades in students.items() if grades["GPA"] < 70}
print("Students with a GPA below 70:", low_gpa_students)



