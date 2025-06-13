# Problem Starement
# Python Implement`lambda`, `generators`, and `iterators` with employee data
#  from Zennial-Pro. covers filtering, mapping, zipping, and yielding values using
#  clean, beginner-friendly code without classes.

# 1. Lambda to square a number
square = lambda x: x ** 2
print("Square of 4:", square(4))  # 16

# 2. Lambda to concatenate names
full_name = lambda f, l: f + " " + l
print("Full Name:", full_name("Amit", "Parse"))

# 3. Lambda inside sorted (sort employees by name length)
employees = ["Amit", "Priya", "Rohit", "Sneha", "Neha"]
sorted_employees = sorted(employees, key=lambda x: len(x))
print("Sorted by name length:", sorted_employees)

# 4. Filter employees with name length > 4
filtered = list(filter(lambda x: len(x) > 4, employees))
print("Names longer than 4 characters:", filtered)

# 5. Map names to uppercase using lambda
upper_names = list(map(lambda x: x.upper(), employees))
print("Uppercase Names:", upper_names)

# 6. Generate list of email IDs using map
emails = list(map(lambda name: f"{name.lower()}@zennialpro.com", employees))
print("Email IDs:", emails)

# 7. Use lambda in list comprehension to tag departments
departments = ["Tech", "HR", "Finance", "Marketing", "Tech"]
tags = [lambda d=dept: f"{d} Department" for dept in departments]
print("Tagged Depts:", [tag() for tag in tags])  # deferred evaluation

# 8. Generator expression to yield even numbers
evens = (x for x in range(10) if x % 2 == 0)
print("Even Numbers:", list(evens))

# 9. Generator that yields squares of employees' ID (1-based)
def employee_id_squares():
    for i in range(1, len(employees)+1):
        yield i ** 2

print("Employee ID Squares:", list(employee_id_squares()))

# 10. Basic iterator usage on list
emp_iter = iter(employees)
print("Next Employee:", next(emp_iter))
print("Next Employee:", next(emp_iter))

# 11. Create dictionary of employee:dept
emp_dict = dict(zip(employees, departments))
print("Employee Dictionary:", emp_dict)

# 12. Lambda to extract first character of each name
initials = list(map(lambda x: x[0], employees))
print("Initials:", initials)

# 13. Use filter to find Tech department employees
tech_emp = list(filter(lambda x: emp_dict[x] == "Tech", employees))
print("Tech Employees:", tech_emp)

# 14. Use map to add suffix to departments
dept_suffix = list(map(lambda d: d + " Dept", departments))
print("Modified Departments:", dept_suffix)

# 15. Generator function to yield emails
def email_gen():
    for emp in employees:
        yield f"{emp.lower()}@zennialpro.com"

print("Emails via generator:", list(email_gen()))

# 16. Use lambda with all() to validate name length > 2
print("All names valid length:", all(map(lambda x: len(x) > 2, employees)))

# 17. Lambda with reduce to combine all names
from functools import reduce
all_names = reduce(lambda x, y: x + ", " + y, employees)
print("Combined Names:", all_names)

# 18. Generator that yields employee-department pairs
def emp_info_gen():
    for e, d in emp_dict.items():
        yield f"{e} → {d}"

print("Employee Info:")
for info in emp_info_gen():
    print("-", info)

# 19. Lambda to reverse names
reversed_names = list(map(lambda x: x[::-1], employees))
print("Reversed Names:", reversed_names)

# 20. Use zip + lambda to print formatted strings
print("Formatted Strings:")
list(map(lambda x: print(f"{x[0]} works in {x[1]}"), zip(employees, departments)))