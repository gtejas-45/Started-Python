
def log_operation(func):
    def wrapper(*args, **kwargs):
        print("\nOperation:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.tasks = []

    def get_role_details(self):
        return "General Employee"

    def calculate_workload(self):
        return len(self.tasks)


class Developer(Employee):
    def __init__(self, emp_id, name, department, language):
        super().__init__(emp_id, name, department)
        self.language = language

    def get_role_details(self):
        return "Developer - " + self.language

    def calculate_workload(self):
        return len(self.tasks) * 2


class DataScientist(Employee):
    def __init__(self, emp_id, name, department, tool):
        super().__init__(emp_id, name, department)
        self.tool = tool

    def get_role_details(self):
        return "Data Scientist - " + self.tool

    def calculate_workload(self):
        return len(self.tasks) * 3


class Manager(Employee):
    def __init__(self, emp_id, name, department, team_size):
        super().__init__(emp_id, name, department)
        self.team_size = team_size

    def get_role_details(self):
        return "Manager - Team Size: " + str(self.team_size)

    def calculate_workload(self):
        return len(self.tasks) + self.team_size


class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1
            return employee
        else:
            raise StopIteration


def task_generator(employees):
    for employee in employees:
        for task in employee.tasks:
            yield employee.name + " -> " + task


@log_operation
def assign_task(employee, task):
    employee.tasks.append(task)
    print("Task assigned successfully.")


employees = []


def create_employee():
    print("\n1. Developer")
    print("2. Data Scientist")
    print("3. Manager")

    choice = input("Enter employee type: ")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")

    if choice == "1":
        language = input("Enter Programming Language: ")
        employee = Developer(emp_id, name, department, language)

    elif choice == "2":
        tool = input("Enter Data Science Tool: ")
        employee = DataScientist(emp_id, name, department, tool)

    elif choice == "3":
        team_size = int(input("Enter Team Size: "))
        employee = Manager(emp_id, name, department, team_size)

    else:
        print("Invalid choice.")
        return

    employees.append(employee)
    print("Employee created successfully.")


def view_employees():
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    iterator = EmployeeIterator(employees)

    print("\nEmployee Details")

    for employee in iterator:
        print("-------------------------")
        print("ID:", employee.emp_id)
        print("Name:", employee.name)
        print("Department:", employee.department)
        print("Role:", employee.get_role_details())
        print("Tasks:", len(employee.tasks))
        print("Workload:", employee.calculate_workload())


def assign_employee_task():
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    emp_id = input("Enter Employee ID: ")

    for employee in employees:
        if employee.emp_id == emp_id:
            task = input("Enter Task: ")
            assign_task(employee, task)
            return

    print("Employee not found.")


def process_tasks():
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    print("\nEmployee Tasks")

    generator = task_generator(employees)

    found = False

    for task in generator:
        print(task)
        found = True

    if not found:
        print("No tasks found.")


def employee_report():
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    print("\nEmployee Report")

    for employee in employees:
        print("-------------------------")
        print("Employee:", employee.name)
        print("Role:", employee.get_role_details())
        print("Number of Tasks:", len(employee.tasks))
        print("Workload:", employee.calculate_workload())


while True:
    print("\n========== Employee Task Management System ==========")
    print("1. Create Employee")
    print("2. Assign Task")
    print("3. View Employees")
    print("4. Process Tasks")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_employee()

    elif choice == "2":
        assign_employee_task()

    elif choice == "3":
        view_employees()

    elif choice == "4":
        process_tasks()

    elif choice == "5":
        employee_report()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")


###  Output


# ========== Employee Task Management System ==========
# 1. Create Employee
# 2. Assign Task
# 3. View Employees
# 4. Process Tasks
# 5. Generate Report
# 6. Exit

# Enter your choice: 1

# 1. Developer
# 2. Data Scientist
# 3. Manager

# Enter employee type: 1
# Enter Employee ID: E101
# Enter Name: Tejas
# Enter Department: IT
# Enter Programming Language: Python

# Employee created successfully.


# Enter your choice: 2
# Enter Employee ID: E101

# Operation: assign_task
# Enter Task: Develop Employee System
# Task assigned successfully.


# Enter your choice: 3

# Employee Details
# -------------------------
# ID: E101
# Name: Tejas
# Department: IT
# Role: Developer - Python
# Tasks: 1
# Workload: 2


# Enter your choice: 4

# Employee Tasks
# Tejas -> Develop Employee System


# Enter your choice: 5

# Employee Report
# -------------------------
# Employee: Tejas
# Role: Developer - Python
# Number of Tasks: 1
# Workload: 2


