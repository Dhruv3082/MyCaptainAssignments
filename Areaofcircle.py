# We are going to find area of circle of radius which will be provided by user

# Assign the value of radius by user input
from cmath import pi


r = float(input('The Radius of the circle : '))

# Write the formula to find area
area = pi*r*r

# Get the area as output
print("The area of the circle with radius", r, "is", area)

#use different method to print
print("The area of the circle with radius {0} is {1}".format(r,area))
