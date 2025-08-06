import math
def square (side_sq):
   return math.ceil(side_sq*side_sq)
size_sq = float (input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(size_sq)}")
