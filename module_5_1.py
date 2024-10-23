class House: # Создаем Класс
    def __init__(self, name, number_is_floors): # Метод и атрибуты
        self.name = name
        self.number_is_floors = number_is_floors



    def go_to(self, new_floors): #  Создаем Метод
        if 1 <= new_floors <= self.number_is_floors: # Проверяем существует ли этаж
            for i in range(1, new_floors + 1):
                print(i) # Вывыодим номера этажей от 1 до заданого
            else:
                print('Такого этаже не существует')
# созадем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# Вызов метода go_to
h1.go_to(5)
h2.go_to(10)