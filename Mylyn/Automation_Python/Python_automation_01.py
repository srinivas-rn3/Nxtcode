#Example: Calculating Total Score Using enumerate

# Sample grades list
grades = ['A', 'B', 'C', 'A', 'A', 'B', 'C']

total_score = 0 

# Define grade points dictionary
grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}


# Calculate total score using enumerate
for index ,grade in enumerate(grades,start=1):
    if grade in grade_points:
        total_score += grade_points[grade]
    else:
        print(f"Invalid grade '{grade}' at index {index}")

# Print total score
print(f"Total Score: {total_score}")

'''
print(grades)
print(grade_points)
for index,grade in enumerate(grades,start=1):
    print(grade_points[grade])
'''