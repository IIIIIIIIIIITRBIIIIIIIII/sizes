is_running =True

circles = []

circle = int(input("How many circles do you want? "))

for i in range(circle):
    d = float(input(f"Enter diameter for circle {i + 1}: "))
    pi = 3.14
    circles.append((d, pi))

for idx, (d, pi) in enumerate(circles):
    s = pi * d
    print(f"Circle {idx + 1} circumference is: {s} cm")

totalCircleSize = 0
for (d, pi) in circles:
    totalCircleSize += pi * d
    print(f"your total cirle size is {totalCircleSize} cm")


a = 0
b = 0
c = 0

triangles = []

triangle = int(input("how many triangles you want? "))

for x in range(triangle):
    a = float(input("enter number a "))
    b = float(input("enter number b "))
    c = float(input("enter number c"))
    triangles.append((a, b, c))

for idx, (a, b, c) in enumerate(triangles):
    s2 = a + b + c
    print(f"triangle {idx + 1} circumference is: {s2} cm")

totalTriangleSize = 0
for (a, b, c) in triangles:
    totalTriangleSize += a + b + c
    print(f"your total triangle size is {totalTriangleSize} cm")

while is_running:
    do = input("Do you want to calculate the size of both together? Y/N: ")

    if do.lower() != "y" and do.lower() != "n":
        print("Invalid answer, please enter Y or N.")
    elif do.lower() == "y":
        totalSize = totalCircleSize + totalTriangleSize
        print(f"The total size is {totalSize} cm")
        is_running = False
    elif do.lower() == "n":
        print("You quit")
        is_running = False
 

    
