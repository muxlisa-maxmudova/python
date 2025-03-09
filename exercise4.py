import math

# C = 2PIR

radius = float(input('Radius of circle in cm: '))
circumference = round(2*math.pi*radius,2)
print(f'C = {circumference} cm')
