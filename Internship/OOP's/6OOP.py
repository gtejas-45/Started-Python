#method overloading is not possible in python
# def f1():
#     print("f1")
# def f1(a):
#     print("f2")
# f1(2)#it print f2 correctly 
# f1() #it gives the error it is not like java .. it don't overloading the method positional arg error give 

class Student:
    college = "SNJB"

    def __init__(self, name):
        self.name = name
student1 = Student("Tejas")
student2 = Student("Rahul")
print(student1.college)
print(student2.college)