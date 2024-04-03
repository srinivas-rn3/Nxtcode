import json 
'''
# Sample JSON data
'''
json_data = '''{
  "students": [
    {
      "name": "John",
      "age": 20,
      "grade": "A"
    },
    {
      "name": "Alice",
      "age": 22,
      "grade": "B"
    },
    {
      "name": "Bob",
      "age": 21,
      "grade": "C"
    }
  ]
}
'''
'''
# Load JSON data into a Python data structure
data = json.loads(json_data)

# Querying JSON data
# Example: Get the names of all students
student_name = [student['name'] for student in data['students']]
print("Student Name:",student_name)

# Example: Filter students who are older than 21
student_above_21 = [student for student in data['students'] if student['age'] >= 21]
print("studetn above 21 are:",student_above_21)
'''

# Load JSON data from file
with open(r"C:\Users\srini\OneDrive\Documents\pythonFiles\emp_py_json.json",'r') as jf:
    data = json.load(jf)

## Example query: Get the names of all employees
emp_names = [employee['name'] for employee in data['employees']]
print("employees names:",emp_names)

# Example query: Get the total salary budget for the company
total_salary_budget = sum(employee['salary'] for employee in data['employees'])
print("Total Salary Budget",f"{total_salary_budget:,}")

# Example query: Filter employees in the Engineering department
engineering_employee = [employee for employee in data['employees'] if employee['department'] =='Engineering']
print("Engineering Employee:", engineering_employee)



