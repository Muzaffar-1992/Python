## 1. Circle Class
## Write a Python program to create a class 
## representing a Circle. Include methods to calculate its area and perimeter.

import math  # matematik funksiyalar uchun (π - pi dan foydalanamiz)

class Circle:
    def __init__(self, radius):
        self.radius = radius  # doiraning radiusi

    def area(self):
        # Doiraning yuzi formulasi: π * r²
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Doiraning uzunligi (aylana uzunligi) formulasi: 2 * π * r
        return 2 * math.pi * self.radius
    
    circle1 = Circle(5)  # radius = 5 bo'lgan doira

    print("Doiraning yuzi:", circle1.area())
    print("Doiraning aylana uzunligi:", circle1.perimeter())


## 2. Person Class
## Write a Python program to create a Person class. Include attributes like name, country, 
## and date of birth. Implement a method to determine the person's age.
from datetime import date  # hozirgi sana va tug'ilgan sanani solishtirish uchun

class Person:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date  # tug‘ilgan sana (format: YYYY-MM-DD)

    def calculate_age(self):
        today = date.today()  # bugungi sana
        # yoshni hisoblash
        age = today.year - self.birth_date.year
        
        # agar tug‘ilgan kuni hali bu yilda bo‘lmagan bo‘lsa, 1 yoshni kamaytirish
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age


# Misol uchun ishlatish:
person1 = Person("Ali", "Uzbekistan", date(2000, 5, 10))

print("Ismi:", person1.name)
print("Davlati:", person1.country)
print("Tug‘ilgan sana:", person1.birth_date)
print("Yoshi:", person1.calculate_age())


## 3. Calculator Class
## Write a Python program to create a Calculator class.
## Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b  # Qo‘shish

    def subtract(self, a, b):
        return a - b  # Ayirish

    def multiply(self, a, b):
        return a * b  # Ko‘paytirish

    def divide(self, a, b):
        if b != 0:
            return a / b  # Bo‘lish
        else:
            return "Xatolik: 0 ga bo‘lish mumkin emas!"
            

# Misol uchun ishlatish:
calc = Calculator()

x = 10
y = 5

print("Qo‘shish:", calc.add(x, y))
print("Ayirish:", calc.subtract(x, y))
print("Ko‘paytirish:", calc.multiply(x, y))
print("Bo‘lish:", calc.divide(x, y))


## 4. Shape and Subclasses
## Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
## Implement subclasses for different shapes like Circle, Triangle, and Square.
import math

# 🔹 Asosiy klass — Shape
class Shape:
    def area(self):
        return 0  # Asosiy shaklda aniqlanmagan

    def perimeter(self):
        return 0  # Asosiy shaklda aniqlanmagan


# 🔹 Circle (Doira) klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # π * r²

    def perimeter(self):
        return 2 * math.pi * self.radius  # 2πr


# 🔹 Square (Kvadrat) klassi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2  # a²

    def perimeter(self):
        return 4 * self.side  # 4a


# 🔹 Triangle (Uchburchak) klassi
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron formulasi: √(s(s-a)(s-b)(s-c)), s = (a+b+c)/2
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# 🔹 Misollar:
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("🔸 Doira: Yuzi =", round(circle.area(), 2), ", Perimetri =", round(circle.perimeter(), 2))
print("🔸 Kvadrat: Yuzi =", square.area(), ", Perimetri =", square.perimeter())
print("🔸 Uchburchak: Yuzi =", triangle.area(), ", Perimetri =", triangle.perimeter())

## 5. Binary Search Tree Class
## Write a Python program to create a class representing a binary search tree. 
## Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # chap bola
        self.right = None  # o‘ng bola


# 🔹 Binary Search Tree (BST) klassi
class BinarySearchTree:
    def __init__(self):
        self.root = None  # boshlanishda daraxt bo‘sh bo‘ladi

    def insert(self, value):
        # Yangi qiymatni daraxtga qo‘shish
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        # Rekursiv yordamchi funksiya
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)
        # Agar qiymat teng bo‘lsa — BST’da takror qiymat qo‘shilmaydi

    def search(self, value):
        # Daraxtda qiymatni qidirish
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False  # topilmadi
        if current.value == value:
            return True   # topildi
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def inorder(self):
        # Daraxtni tartib bilan chiqarish (eng kichikdan kattaga)
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


# 🔹 Misol uchun ishlatish:
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    bst.insert(v)

print("Daraxtdagi elementlar (inorder):", bst.inorder())
print("60 soni daraxtda bormi?", bst.search(60))
print("25 soni daraxtda bormi?", bst.search(25))

Node klassi
— Daraxtdagi har bir tugunni ifodalaydi:
har bir tugunda value, left, va right mavjud.

BinarySearchTree klassi

root → daraxtning boshlang‘ich tuguni.

insert() → yangi tugun qo‘shadi.

search() → berilgan qiymat daraxtda bor-yo‘qligini tekshiradi.

inorder() → daraxtni kichikdan kattagacha tartibda chiqaradi.

_insert() va _search()
— bu yordamchi rekursiv funksiyalar (ya’ni, o‘zini o‘zi chaqiradi).

BST qoidasiga ko‘ra:

Agar yangi qiymat kichik bo‘lsa → chapga ketadi.

Agar katta bo‘lsa → o‘ngga ketadi.

## 6. Stack Data Structure
## Write a Python program to create a class representing a stack data structure.
## Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []  # steck elementlarini ro‘yxatda saqlaymiz

    def is_empty(self):
        # steck bo‘shligini tekshirish
        return len(self.items) == 0

    def push(self, item):
        # elementni steckning ustiga qo‘shish
        self.items.append(item)

    def pop(self):
        # eng oxirgi elementni olib tashlash va qaytarish
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Xatolik: Stack bo‘sh!"

    def peek(self):
        # eng ustki elementni qaytarish (olmay)
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bo‘sh!"

    def size(self):
        # stackdagi elementlar soni
        return len(self.items)


# 🔹 Misol uchun ishlatish:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack holati:", stack.items)
print("Eng ustki element:", stack.peek())
print("Olib tashlangan element:", stack.pop())
print("Yangi stack holati:", stack.items)
print("Stack hajmi:", stack.size())

## 7. Linked List Data Structure
## Write a Python program to create a class representing a linked list data structure. Include methods 
## for displaying linked list data, inserting, and deleting nodes.

## 8. Shopping Cart Class
## Write a Python program to create a class representing a shopping cart.
## Include methods for adding and removing items, and calculating the total price.



class ShoppingCart:
    def __init__(self):
        self.items = {}  # mahsulotlar dict ko‘rinishida saqlanadi: {"mahsulot": [narx, miqdor]}

    def add_item(self, product, price, quantity=1):
        # Savatga mahsulot qo‘shish
        if product in self.items:
            self.items[product][1] += quantity  # agar bor bo‘lsa, miqdorni oshiramiz
        else:
            self.items[product] = [price, quantity]
        print(f"{product} savatga qo‘shildi. ({quantity} dona)")

    def remove_item(self, product):
        # Savatdan mahsulotni o‘chirish
        if product in self.items:
            del self.items[product]
            print(f"{product} savatdan o‘chirildi.")
        else:
            print(f"{product} savatda topilmadi.")

    def calculate_total(self):
        # Umumiy narxni hisoblash
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def show_cart(self):
        # Savatdagi mahsulotlarni chiqarish
        if not self.items:
            print("Savat bo‘sh.")
            return
        print("🛍️ Savatdagi mahsulotlar:")
        for product, (price, quantity) in self.items.items():
            print(f"- {product}: {quantity} dona x {price} so‘m = {price * quantity} so‘m")
        print(f"💰 Umumiy summa: {self.calculate_total()} so‘m")


# 🔹 Misol uchun ishlatish:
cart = ShoppingCart()

cart.add_item("Olma", 5000, 3)
cart.add_item("Banan", 7000, 2)
cart.add_item("Olma", 5000, 1)  # miqdor oshadi

cart.show_cart()

cart.remove_item("Banan")
cart.show_cart()

## 9. Stack with Display
## Write a Python program to create a class representing a stack data structure.
#  Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.items = []  # Stack elementlarini saqlash uchun ro‘yxat

    def is_empty(self):
        # Stack bo‘shligini tekshirish
        return len(self.items) == 0

    def push(self, item):
        # Stackga element qo‘shish (ustiga)
        self.items.append(item)
        print(f"{item} stackga qo‘shildi.")

    def pop(self):
        # Stackdan eng oxirgi elementni olib tashlash
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} stackdan olib tashlandi.")
        else:
            print("Xatolik: Stack bo‘sh!")

    def display(self):
        # Stackdagi elementlarni ko‘rsatish
        if self.is_empty():
            print("Stack bo‘sh.")
        else:
            print("Stack elementlari (ustdan pastga):")
            for item in reversed(self.items):  # eng yuqoridagidan pastdagigacha
                print(item)


# 🔹 Misol uchun ishlatish:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()


## 10. Queue Data Structure
## Write a Python program to create a class representing a queue data structure.
## Include methods for enqueueing and dequeueing elements.
