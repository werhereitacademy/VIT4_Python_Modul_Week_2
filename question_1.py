# question 2 Öğrenci Notları İşleme
students = {
    'Pieter van der Berg': [80, 90, 85],
    'Lotte Bakker': [65, 75, 70],
    'Eva Jansen': [70, 85, 80],
    'Daan van Dijk': [55, 60, 65],
    'Sofie Kramer': [90, 95, 92],
    'Lucas Hoekstra': [75, 80, 78],
    'Fleur van Leeuwen': [85, 88, 87],
    'Ties Smeets': [78, 82, 80],
    'Mila van Gogh': [92, 94, 93],
    'Noah de Vries': [60, 70, 65]
}

# 1. Calculate the average score for each student and add it to the dictionary.
for scores_list in students.values():
    average_score = ((sum(scores_list) * 10) // len(scores_list)) / 10
    scores_list.append(average_score)

# 2. Find the student with the highest average score and print it.
highest_average = 0
best_student = ""
for name, scores_list in students.items():
    average_score = scores_list[3]
    if average_score > highest_average:
        highest_average = average_score
        best_student = name
print("Student with the highest average score:", best_student)

# 3. Separate the first name and last name of each student and store them in a list of tuples.
full_names = []
for name in students.keys():
    full_names.append(tuple(name.split()))
print("List of tuples with first and last names:", full_names)

# 4. Sort the first names alphabetically and print the sorted list.
sorted_firstnames = sorted(i[0] for i in full_names)
print("Sorted list of first names:", sorted_firstnames)

# 5. Store students with an average score below 70 in a set.
below70 = set()
for name, scores in students.items():
    if scores[-1] < 70:
        below70.add(name)
print("Students with an average score below 70:", below70)
