students = [
    {"name": "Ahmed", "grades": [85, 90, 78]},
    {"name": "Sara", "grades": [92, 88, 95]},
    {"name": "Mohamed", "grades": [75, 80, 72]},
    {"name": "Fatima", "grades": [88, 92, 85]}
]

print("===== Student Grades Report =====")

for student in students:
    name = student["name"]
    
    grades = student["grades"]
    
    average = sum(grades) / len(grades)
    
    print(f"{name}: Average = {average:.2f}")