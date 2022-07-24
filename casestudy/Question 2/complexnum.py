'''A. Write a python program to perform the following operations on complex numbers by
creating a class complex_number. Create two objects c1 and c2.
a. Addition
b. Subtraction
c. Multiplication
d. Check if two complex numbers are equal or not
e. Check if c1>=c2
f. Check if c1==c2
Perform these operations using operator overloading in python.'''
class complex_number:
    def __init__(self,number):
        self.number=number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __eq__(self, other):
        return self.number == other.number

    def __ge__(self, other):
        return abs(self.number) >= abs(other.number)

    def __le__(self, other):
        return abs(self.number) <= abs(other.number)

print("Enter two complex numbers:")
num1=complex(input())
num2=complex(input())

c1=complex_number(num1)
c2=complex_number(num2)

sum = c1 +c2
print("Addition of {0} and {1} : {2}".format(num1,num2,sum))

sub = c1 - c2
print("Subtraction of {0} and {1} : {2}".format(num1,num2,sub))

multi = c1*c2
print("Multiplication of {0} and {1} : {2}".format(num1,num2,multi))

equal=(c1==c2)
print("{0} and {1} are equal : {2}".format(num1,num2,equal))

greater = (c1>=c2)
print("{0} is greater than equal to {1} : {2}".format(num1,num2,greater))


less = (c1<=c2)
print("{0} is less than equal to {1} : {2}".format(num1,num2,less))




    