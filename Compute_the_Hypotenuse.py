#Compute_the_Hypotenuse
from math import sqrt
a = int(input("Enter the first shorter side of the right triangle: "))
b = int(input("Enter the second shorter side of the right triangle: "))
def last_length (a,b):
    return sqrt(a ** 2 + b ** 2)
print ("The length of the hypotenuse is: " + str(last_length(a,b)))