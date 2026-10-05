class Employee:
    Company_Name = "CodeSpyder Technologies"
    Employee_Count = 50
    
    
    def __init__(self,Employee_ID,Name,Department,Basic_Salary):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.Department = Department
        self.Basic_Salary = Basic_Salary
        Employee.Employee_Count += 1
        
    def cal_annual_salary(self):
        annual_Salary = self.Basic_Salary * 12
        return annual_Salary
    
    def give_bonus(self,percentage):
        bonus = self.Basic_Salary * percentage / 100
        # self.Basic_Salary += bonus
        # return self.Basic_Salary
        return bonus
    
    def __str__(self):
        return (
            f"Employee ID : {self.Employee_ID}\n"
            f"Name        : {self.Name}\n"
            f"Department  : {self.Department}\n"
            f"Basic Salary: {self.Basic_Salary}"
        )
    
    def __len__(self):
        return len(self.Name)
    
    
    
emp1 = Employee(1,"Raj","Computer",20000)
print(emp1)

# Calculate annual salary
print("Annual Salary :", emp1.cal_annual_salary())


# Give 10% bonus
print("Bonus :", emp1.give_bonus(10))


# __len__()
print("Employee Name Length :", len(emp1))


# Class variable
print("Company :", Employee.Company_Name)


# Class variable
print("Employee Count :", Employee.Employee_Count)
        
# OUTPUT----------------------

# Employee ID : 1
# Name        : Raj
# Department  : Computer
# Basic Salary: 20000
# Annual Salary : 240000
# Bonus : 2000.0
# Employee Name Length : 3
# Company : CodeSpyder Technologies
# Employee Count : 51

# ---------------------------------