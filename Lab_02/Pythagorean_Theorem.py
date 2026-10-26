def distan_formula(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5   
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance = distan_formula(x1, y1, x2, y2)
print(f"The distance between the two points is: {distance}")