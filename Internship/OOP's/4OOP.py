# ============================================================
# PYTHON OOP - DUNDER METHODS / MAGIC METHODS
# Example: Complex Number Class
# ============================================================


# ------------------------------------------------------------
# 1. CREATING A CLASS
# ------------------------------------------------------------

class Complex:

    # --------------------------------------------------------
    # CLASS VARIABLE
    # --------------------------------------------------------
    # 'count' belongs to the CLASS, not to individual objects.
    #
    # We access it using:
    #     Complex.count
    #
    # It will keep track of how many Complex objects are created.
    # --------------------------------------------------------

    count = 0


    # --------------------------------------------------------
    # 2. __init__() --> CONSTRUCTOR
    # --------------------------------------------------------
    # __init__ is a DUNDER METHOD.
    #
    # DUNDER means:
    # Double UNDERscore
    #
    # __init__ has double underscores before and after 'init'.
    #
    # Python automatically calls __init__() when we create
    # an object.
    #
    # Example:
    #
    # c1 = Complex(3, 2)
    #
    # Python internally calls:
    #
    # Complex.__init__(c1, 3, 2)
    #
    # self refers to the current object.
    # --------------------------------------------------------

    def __init__(self, x, y):

        # self.real belongs to the current object.
        #
        # If:
        # c1 = Complex(3, 2)
        #
        # then:
        # self.real = 3
        # means:
        # c1.real = 3

        self.real = x

        # Similarly:
        # c1.imag = 2

        self.imag = y


        # ----------------------------------------------------
        # INCREASING THE CLASS VARIABLE
        # ----------------------------------------------------
        # Every time an object is created, count increases by 1.
        #
        # Complex.count means:
        # access the class variable 'count'
        #
        # Example:
        #
        # First object  --> count = 1
        # Second object --> count = 2
        # Third object  --> count = 3
        # ----------------------------------------------------

        Complex.count = Complex.count + 1



    # --------------------------------------------------------
    # 3. __add__() --> ADDITION DUNDER METHOD
    # --------------------------------------------------------
    # __add__ is called automatically when we use '+'
    #
    # Example:
    #
    # c3 = c1 + c2
    #
    # Python internally converts this into:
    #
    # c3 = c1.__add__(c2)
    #
    # self = c1
    # x    = c2
    #
    # So we can access:
    #
    # self.real --> c1.real
    # x.real    --> c2.real
    # --------------------------------------------------------

    def __add__(self, x):

        # Add the real parts.
        #
        # If:
        # c1 = 3 + 2i
        # c2 = 1 + 5i
        #
        # Then:
        #
        # a = 3 + 1
        # a = 4

        a = self.real + x.real


        # Add the imaginary parts.
        #
        # b = 2 + 5
        # b = 7

        b = self.imag + x.imag


        # Create a NEW Complex object using the result.
        #
        # Complex(4, 7)
        #
        # This creates a new object containing:
        #
        # real = 4
        # imag = 7

        return Complex(a, b)



    # --------------------------------------------------------
    # 4. __lt__() --> LESS THAN DUNDER METHOD
    # --------------------------------------------------------
    # __lt__ means "LESS THAN".
    #
    # It is automatically called when we use:
    #
    # <
    #
    # Example:
    #
    # p = c1 < c2
    #
    # Python internally calls:
    #
    # p = c1.__lt__(c2)
    #
    # self = c1
    # x    = c2
    # --------------------------------------------------------

    def __lt__(self, x):

        # Calculate the square of the magnitude of self.
        #
        # For a complex number:
        #
        # a + bi
        #
        # magnitude squared = a² + b²
        #
        # We are using:
        #
        # real² + imaginary²

        m1 = self.real**2 + self.imag**2


        # Calculate the square of the magnitude of x.

        m2 = x.real**2 + x.imag**2


        # Compare both values.
        #
        # If m1 is smaller than m2:
        # return True
        #
        # Otherwise:
        # return False

        return m1 < m2



    # --------------------------------------------------------
    # 5. __str__() --> STRING REPRESENTATION DUNDER METHOD
    # --------------------------------------------------------
    # __str__ is automatically called when we use:
    #
    # print(object)
    #
    # or:
    #
    # str(object)
    #
    # Example:
    #
    # print(c1)
    #
    # Python internally calls:
    #
    # c1.__str__()
    #
    # IMPORTANT:
    # __str__ MUST RETURN A STRING.
    # --------------------------------------------------------

    def __str__(self):

        # This print is executed when __str__() is called.
        #
        # So:
        #
        # print(c1)
        #
        # will first execute this line.

        print('****')


        # format() inserts the values of real and imag
        # into the string.
        #
        # {} --> placeholder
        #
        # First {} --> self.real
        # Second {} --> self.imag
        #
        # Example:
        #
        # self.real = 3
        # self.imag = 2
        #
        # Result:
        #
        # "3+2i"

        return '{}+{}i'.format(self.real, self.imag)



# ============================================================
# OBJECT CREATION
# ============================================================


# ------------------------------------------------------------
# 6. FIRST OBJECT
# ------------------------------------------------------------
# Complex(3, 2) calls __init__(self, 3, 2)
#
# c1.real = 3
# c1.imag = 2
#
# count becomes 1
# ------------------------------------------------------------

c1 = Complex(3, 2)


# ------------------------------------------------------------
# 7. SECOND OBJECT
# ------------------------------------------------------------
# Complex(1, 5) calls __init__(self, 1, 5)
#
# c2.real = 1
# c2.imag = 5
#
# count becomes 2
# ------------------------------------------------------------

c2 = Complex(1, 5)



# ============================================================
# __add__() WORKING
# ============================================================

# ------------------------------------------------------------
# 8. ADDING TWO OBJECTS
# ------------------------------------------------------------
#
# c3 = c1 + c2
#
# Python automatically calls:
#
# c3 = c1.__add__(c2)
#
# Inside __add__:
#
# self = c1
# x    = c2
#
# Real:
# 3 + 1 = 4
#
# Imaginary:
# 2 + 5 = 7
#
# So:
#
# c3 = Complex(4, 7)
#
# Creating c3 also calls __init__().
#
# Therefore count becomes 3.
# ------------------------------------------------------------

c3 = c1 + c2


# ============================================================
# __lt__() WORKING
# ============================================================

# ------------------------------------------------------------
# 9. COMPARING TWO OBJECTS
# ------------------------------------------------------------
#
# p = c1 < c2
#
# Python automatically calls:
#
# p = c1.__lt__(c2)
#
#
# For c1 = 3 + 2i:
#
# m1 = 3² + 2²
# m1 = 9 + 4
# m1 = 13
#
#
# For c2 = 1 + 5i:
#
# m2 = 1² + 5²
# m2 = 1 + 25
# m2 = 26
#
#
# Now:
#
# 13 < 26
#
# Therefore:
#
# p = True
# ------------------------------------------------------------

p = c1 < c2


# ------------------------------------------------------------
# To see the result of __lt__():
#
# print(p)
#
# Output:
# True
# ------------------------------------------------------------

# print(p)



# ============================================================
# __str__() WORKING
# ============================================================

# ------------------------------------------------------------
# 10. print(c1)
# ------------------------------------------------------------
#
# When we write:
#
# print(c1)
#
# Python does NOT know directly how to print our Complex
# object.
#
# Therefore Python calls:
#
# c1.__str__()
#
# Inside __str__():
#
# print('****')
#
# is executed first.
#
# Then:
#
# return '{}+{}i'.format(self.real, self.imag)
#
# returns:
#
# 3+2i
#
# So output will be:
#
# ****
# 3+2i
# ------------------------------------------------------------

print(c1)



# ============================================================
# FINAL CONCEPT SUMMARY
# ============================================================

# ------------------------------------------------------------
# DUNDER METHODS USED IN THIS PROGRAM
# ------------------------------------------------------------
#
# 1. __init__()
#    --> Constructor
#    --> Called automatically when object is created.
#
#    Example:
#    c1 = Complex(3, 2)
#
#
# 2. __add__()
#    --> Controls '+' operator for objects.
#
#    Example:
#    c3 = c1 + c2
#
#    Internally:
#    c3 = c1.__add__(c2)
#
#
# 3. __lt__()
#    --> Controls '<' operator for objects.
#
#    Example:
#    p = c1 < c2
#
#    Internally:
#    p = c1.__lt__(c2)
#
#
# 4. __str__()
#    --> Controls how an object is represented as a string.
#
#    Example:
#    print(c1)
#
#    Internally:
#    c1.__str__()
#
#
# ============================================================
# IMPORTANT DUNDER METHOD PATTERN
# ============================================================
#
# Python operator       Dunder method
# ------------------------------------
# +                     __add__()
# -                     __sub__()
# *                     __mul__()
# /                     __truediv__()
# <                     __lt__()
# >                     __gt__()
# ==                    __eq__()
# !=                    __ne__()
# <=                    __le__()
# >=                    __ge__()
# print(object)         __str__()
# object creation       __init__()
#
#
# The important idea is:
#
# Python operators can be given special behavior for our
# objects by defining the corresponding dunder method.
#
# ============================================================