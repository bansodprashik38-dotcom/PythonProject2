a = int(input("enter side of square:"))
b = a * a
print("area of square is", b)

base = int(input("enter base of trangle"))
height = int(input("enter height of trangle"))
area = 0.5 * base * height
print("area of trangle is", area)

length = int(input("enter length of rectangle"))
breadth = int(input("enter breadth of rectangle"))
area = length * breadth
print("area of rectangle is", area)

radius = int(input("enter radius of circle"))
area = 3.14 * radius * radius
print("area of circle is", area)

d1 = int(input("Enter first diagonal of rhombus: "))
d2 = int(input("Enter second diagonal of rhombus: "))
area = 0.5 * d1 * d2
print("Area of rhombus is", area)

base = int(input("Enter base of parallelogram: "))
height = int(input("Enter height of parallelogram: "))
area = base * height
print("Area of parallelogram is", area)

a = int(input("Enter first parallel side (a): "))
b = int(input("Enter second parallel side (b): "))
h = int(input("Enter height of trapezium: "))
area = ((a + b) * h) / 2
print("Area of trapezium is", area)
