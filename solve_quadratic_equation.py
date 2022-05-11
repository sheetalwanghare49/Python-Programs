#program to solve Quadratic Equation
import cmath
a=2
b=8
c=6
d=(b**2)-(4*a*c)
#two solutions
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print("The solution are {0} and {1}".format(sol1,sol2))
