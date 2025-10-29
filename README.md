# 🧮 Polygon Inheritance Hierarchy (Exercise P-2.39)

## 📘 Description
This project is based on **Exercise P-2.39** from the textbook  
*Data Structures and Algorithms in Python* by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser.

The goal of this exercise is to **demonstrate inheritance, abstraction, and polymorphism** in object-oriented programming using Python classes that represent geometric shapes.

---

## 🧱 Objective
To design an **inheritance hierarchy** for different types of polygons where each shape is represented as a class derived from a common abstract base class called `Polygon`.

---

## 🧩 Requirements

### 1. Base Class – `Polygon`
- Declared as an **abstract class** using Python’s `abc` module.  
- Contains two abstract methods:  
  - `area()`  
  - `perimeter()`  

### 2. Derived Classes
Implement classes that inherit from `Polygon`:
- `Triangle`
- `Quadrilateral`
- `RegularPolygon`
- `Pentagon`
- `Hexagon`
- `Octagon`

Each subclass defines its own formula for `area()` and `perimeter()`.

### 3. Specialized Subclasses
Implement more specific polygons with proper inheritance:
- `IsoscelesTriangle` (inherits from `Triangle`)
- `EquilateralTriangle` (inherits from `Triangle`)
- `Rectangle` (inherits from `Quadrilateral`)
- `Square` (inherits from `Quadrilateral`)

### 4. Program Behavior
- The program allows the user to select a shape type (e.g., Triangle, Rectangle, Square, etc.).  
- It takes relevant inputs (like sides, base, or height).  
- It then calculates and displays the **area** and **perimeter** of the chosen shape.

---

## 🧠 Concepts Demonstrated

| Concept | Description |
|----------|-------------|
| **Abstraction** | The `Polygon` base class hides implementation details by defining abstract methods. |
| **Inheritance** | Subclasses inherit from `Polygon` and other intermediate classes like `Triangle` or `Rectangle`. |
| **Polymorphism** | Each shape implements `area()` and `perimeter()` differently, but they can all be used interchangeably as `Polygon` objects. |
| **Encapsulation** | Each class manages its own attributes (like side lengths) internally. |
| **Instantiation** | Objects of different polygon types are created (instantiated) and operated upon at runtime. |

---

## 🧮 Example Output

```
Choose shape: 1=Triangle, 2=Rectangle, 3=Square, 4=Equilateral Triangle, 5=Pentagon, 6=Hexagon
Enter choice: 5
Enter side: 4
Perimeter = 20.00
Area = 27.53
```

---

## ⚙️ Tools & Technologies
- **Language:** Python 3  
- **Concepts Used:** Classes, Inheritance, Abstract Base Classes, Method Overriding  
- **Modules:** `abc`, `math`

---

## 💬 Optional Extension
For additional functionality, the user can input polygon vertex coordinates to:
- Calculate sides using the distance formula.  
- Compare polygons for **similarity** (equal angles and proportional sides).

---

## 🧾 Author Notes
This exercise reinforces understanding of object-oriented design in Python through a geometric and visual example, helping to grasp **class hierarchies, code reuse, and abstraction principles**.
