
import math
speed = int(input("What is the projectile speed? (m/s) > "))
angle = int(input("What is the angle of the projectile? > "))

g = 9.81

def maxHeight(speed, angle, g):
    height = ((speed ** 2) * math.sin(angle)) / (2 * g)
    return height

def timeToHeight(speed, angle, g):
    timeh = (speed * math.sin(angle)) / g
    return timeh


print("The max height of the projectile will be: " + str(maxHeight(speed, angle, g)) + " meters")
print("The time to reach the max height will be: " + str(timeToHeight(speed, angle, g)) + " seconds")