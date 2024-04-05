students = {
    'John Smith': [87, 95, 90],
    'Emily Johnson': [42, 85, 55],
    'Michael Brown': [68, 82, 90],
    'Jessica Davis': [97, 91, 95],
    'Christopher Wilson': [75, 80, 70],
    'Jennifer Taylor': [32, 53, 70],
    'David Martinez': [72, 56, 80],
    'Sarah Anderson': [68, 84, 85],
    'James Thomas': [50, 59, 80],
    'Mary Garcia': [91, 86, 90]
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
print("The student with the highest average score is ", best_student)

# 3. Separate the first name and last name of each student and store them in a list of tuples.
full_names = []
for name in students.keys():
    full_names.append(tuple(name.split()))

# 4. Sort the names alphabetically and print the sorted list.
sorted_firstnames = sorted(i[0] for i in full_names)
print("First names alphabetically:\n", sorted_firstnames)

# 5. Store students with an average score below 70 in a set.
below70 = set()
for name, scores in students.items():
    if scores[-1] < 70:
        below70.add(name)
