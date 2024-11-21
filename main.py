import math  # Для обчислення відстаней між точками
import matplotlib.pyplot as plt  # Для візуалізації точок

# Завдання 1: Визначення класу Point_1
class Point_1:

    # Змінна класу для відстеження кількості створених екземплярів
    instance_count = 0

    def __init__(self, x=0, y=0):
        # Встановлення координат із перевіркою меж [-100, 100]
        self._x = x if -100 <= x <= 100 else 0
        self._y = y if -100 <= y <= 100 else 0
        Point_1.instance_count += 1

    def __del__(self):
        Point_1.instance_count -= 1
        print(f"Об'єкт {self} знищено")

    # Геттери
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # Сеттери
    @x.setter
    def x(self, value):
        self._x = value if -100 <= value <= 100 else 0

    @y.setter
    def y(self, value):
        self._y = value if -100 <= value <= 100 else 0

    # Метод для зміни координат
    def move(self, dx, dy):
        self.x = self._x + dx
        self.y = self._y + dy

    # Метод класу для отримання кількості екземплярів
    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

    # Метод для відображення інформації про точку
    def __str__(self):
        return f"Point(x={self._x}, y={self._y})"

# Завдання 2: Робота з об'єктами
# Створення списку з трьох точок
point1 = Point_1(20, 30)
point2 = Point_1(50, 60)
point3 = Point_1(-90, 0)

# Обчислення відстані між першою і другою точками
distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
print(f"Відстань між точками: {distance:.2f}")

# Пересування третьої точки на 10 вліво
point3.move(-10, 0)

# Відображення результатів
points_before = [(20, 30), (50, 60), (-90, 0)]
points_after = [(point1.x, point1.y), (point2.x, point2.y), (point3.x, point3.y)]

# Завдання 3: Візуалізація точок
def plot_points(points, title):
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, color='blue', label='Точки')
    for i, (x, y) in enumerate(points, 1):
        plt.text(x, y, f'P{i}', fontsize=12, ha='right')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()

# Відображення точок до змін
plot_points(points_before, "Точки до змін")

# Відображення точок після змін
plot_points(points_after, "Точки після змін")

# Завдання 4: Збереження у текстовий файл
with open("points.txt", "w") as file:
    for i, (x, y) in enumerate(points_after, 1):
        file.write(f"{i}: {x}; {y}\n")
print("Координати точок збережено у файл points.txt")
