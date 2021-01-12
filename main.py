
import matplotlib.pyplot as plt
import math
speed = float(input("What is the projectile speed? (m/s) > "))
angle = float(input("What is the angle of the projectile? > "))

g = 9.81

def maxHeight(speed, angle, g):
    height = ((speed ** 2) * math.sin(angle)) / (2 * g)
    return height

def timeToHeight(speed, angle, g):
    timeh = (speed * math.sin(angle)) / g
    return timeh

def parabool(speed, angle, g, i):
    yfor = float(math.tan(angle)) * i - (g / (float(2) * (speed ** float(2) ) * (float(math.cos(angle))))) * (i ** float(2) )
    return yfor

print("The max height of the projectile will be: " + str(maxHeight(speed, angle, g)) + " meters")
print("The time to reach the max height will be: " + str(timeToHeight(speed, angle, g)) + " seconds")

# x axis values
x = [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
y = []

for i in x:
    yinner = parabool(speed, angle, g, i)
    y.append(yinner)
    print(i)
    print(yinner)


# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - Tijd')
# naming the y axis
plt.ylabel('y - Hoogte')

# giving a title to my graph
plt.title('Projectile Motion')

# function to show the plot
plt.show()