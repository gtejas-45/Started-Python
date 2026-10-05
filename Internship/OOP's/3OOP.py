class Human:
    #class variable --> The variables in a class and we called it by the class name not like object name
    count = 0
    
    #constructor 
    ''' 1.In python we created by using the __init__ keyword Not like other language 
        2.Invoke when object created
        3.Don't have return type other than None , other like str,float,etc gives typeError
        4.In python we cannot create many constructor we can handle it by the object creation'''
    # def __init__(self): #Default constructor - No parameters in this
    #     self.weight = 75
    #     self.height = 160
    
    #self - Used to refer the current object
    
    # def __init__(self,name):  #Parameterize constructor - parameters in this
    #     self.name = name
    
    def __init__(self,weight = 73,height = 170): #Default constructor - No parameters in this
        self.weight = weight  #This weight & height are instance variables so it called by the object
        self.height = height
        Human.count = Human.count + 1 #class variable 
        
    #destructor - delete the object
    def __del__(self):
        Human.count = Human.count - 1
        
        
        
hum1 = Human()
print(hum1.height)
print(hum1.weight)
print(Human.count)

hum2 = Human(89)
print(hum2.height)
print(hum2.weight)
print(Human.count)

hum3 = Human(89,180)
print(hum3.height)
print(hum3.weight)

print("Before",Human.count)

del(hum3) #delete the object hum3
print("After",Human.count)