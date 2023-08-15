# import the pi, tan and cos functions from math module
from math import pi, tan, cos

# declare the variables
height_of_the_barrel = 1
horizontal_distance = 0.5
gravity_acceleration = 9.8
elevation_in_degrees = 80
elevation_in_radians = elevation_in_degrees * (pi/180)
initial_velocity = 44

# calculate the projectile and assign the value to a variable named projectile
projectile = height_of_the_barrel + (horizontal_distance * tan(elevation_in_radians))\
             - ((gravity_acceleration * horizontal_distance ** 2)
                / (2 * (initial_velocity * cos(elevation_in_radians))**2))

# print the value of the variable projectile into the console
print(projectile)
