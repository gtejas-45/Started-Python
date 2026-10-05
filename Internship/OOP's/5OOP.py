#Simple Inheritance
# class A:
#     def __init__(self):
#         self.var1 = 0
#         self.var2 = 10
#     def display(self):
#         print(self.var1,self.var2)
        
# #inherit
# class B(A):
#     def __init__(self):
#         self.var3 = 20
#         super().__init__()
#     def display1(self):
#         print(self.var3)
#         self.display()
        
# b1 = B()
# b1.display() #without creating super we cannot access the var 1 and var2 after creating it in B constructor it calls
# b1.display1()
#------------------------------------------------------------------------------------------------------------   
# class A:
#     def __init__(self,x,y):
#         self.var1 = x
#         self.var2 = y
#     def display(self):
#         print(self.var1,self.var2)
        
# #inherit
# class B(A):
#     def __init__(self):
#         self.var3 = 20
#         super().__init__(10,20) #If there is not default variable you have to pass argument in init like this otherwise it gives errors
#     def display1(self):
#         print(self.var3)
#         self.display()
        
# b1 = B() #if we don't give argument it goes straight and error in the 33 line because the 2 missing arguments
# b1.display() #without creating super we cannot access the var 1 and var2 after creating it in B constructor it calls
# b1.display1()
#------------------------------------------------------------------------------------------------------------ 
# class A:
#     def __init__(self,x,y):
#         self.var1 = x
#         self.var2 = y
#     def display(self):
#         print(self.var1,self.var2)
        
# #inherit
# class B(A):
#     def __init__(self,p,q,r):
#         self.var3 = r
#         super().__init__(p,q) #If there is not default variable you have to pass argument in init like this otherwise it gives errors
#     def display1(self):
#         print(self.var3)
#         self.display()
        
# b1 = B(10,20,30) #if we don't give argument it goes straight and error in the 33 line because the 2 missing arguments
# b1.display() #without creating super we cannot access the var 1 and var2 after creating it in B constructor it calls
# b1.display1()

#------------------------------------------------------------------------------------------------------------ 
# 2)Multilevel
class A:
    def dis(self):
        print("inside A")
class B(A):
    def dis1(self):
        print("Inside B")
class C(B):
    def dis2(self):
        print("Inside c")
        self.dis1()
        self.dis()
        
b1 = C()
b1.dis2()
#------------------------------------------------------------------------------------------------------------ 
# 2)Multiple
class A:
    def dis(self):
        print("inside A")
class B:
    def dis1(self):
        print("Inside B")
class C(B,A):
    def dis2(self):
        print("Inside c")
        self.dis1()
        self.dis()
        
b1 = C()
b1.dis2()
#------------------------------------------------------------------------------------------------------------
#override
class Animal:
    def eat(self):
        print("animal eat")
class Dog(Animal):
    def eat(self):
        print("dog eat")
class Cat(Animal):
    def mew(self):
        print("Mew")
        
c1 = Cat()
d1 = Dog()
d1.eat() #override the method eat 
c1.eat()
#------------------------------------------------------------------------------------------------------------ 
#is_a
class A:
    pass
class B:
    pass
a1 = A()
b1 = B()
print(isinstance(a1,A))
print(isinstance(b1,A))
print(isinstance(a1,B))
print(isinstance(b1,B))
#------------------------------------------------------------------------------------------------------------ 
