import random


# Базовый класс для всех животных
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0  # Степень опасности по умолчанию

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # Координаты в пространстве
        self.speed = speed  # Скорость передвижения

    # Метод для перемещения животного
    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    # Метод для получения текущих координат
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    # Метод для атаки
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # Метод для издания звука
    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("No sound available")


# Класс для птиц, наследуется от Animal
class Bird(Animal):
    beak = True  # Наличие клюва

    # Метод для откладывания яиц
    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Here are(is) {eggs_count} eggs for you")


# Класс для водных животных, наследуется от Animal
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Степень опасности для водных животных

    # Метод для ныряния
    def dive_in(self, dz):
        dz = abs(dz)  # Берем модуль dz
        self._cords[2] -= dz * (self.speed / 2)  # Уменьшаем координату z с учетом скорости
        if self._cords[2] < 0:
            self._cords[2] = 0  # Не позволяем координате z быть меньше 0


# Класс для ядовитых животных, наследуется от Animal
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Степень опасности для ядовитых животных


# Класс для утконоса, наследуется от Bird, AquaticAnimal и PoisonousAnimal
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"  # Звук, который издает утконос


# Пример использования
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
