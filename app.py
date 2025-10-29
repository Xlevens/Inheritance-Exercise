from Hexagon.hexagon import Hexagon
from Pentagon.pentagon import Pentagon
from Quad.Quadrilateral import Quadrilaterals
from Quad.rectangle import Rectangle
from Quad.square import Square
from RegPolygon.regpoly import RegularPolygon
from Triangle.triangle import Triangle
from Triangle.equilateral import Equilaterel
from Triangle.isoceles import Isoceles
from Octagon import octagon

def App():
    print("Choose shape: 1=Triangle, 2=Rectangle, 3=Square, 4=Equilateral Triangle 5=Pentagon 6=Hexagon 7=Octagon")
    choice = int(input("Enter choice: "))

    if choice == 1:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        shape = Triangle(a, b, c)

    elif choice == 2:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        shape = Rectangle(l, w)

    elif choice == 3:
        s = float(input("Enter side: "))
        shape = Square(s)

    elif choice == 4:
        a = float(input("Enter side: A"))
        b = float(input("Enter side: B"))
        c = float(input("Enter side: C"))
        shape = Equilaterel(a,b,c)
    elif choice == 5:
        s = float(input("Enter side: "))
        shape = Pentagon(s)
    elif choice == 6:
        s = float(input("Enter side: "))
        shape = Hexagon(s)
    elif choice == 7:
        s = float(input("Enter side: "))
        shape = Hexagon(s)


    else:
        print("Invalid choice")
        return

    print(f"Perimeter = {shape.perimeter():.2f}")
    print(f"Area = {shape.area():.2f}")

