class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 18)  # Создание объектов класса House
h2 = House('Домик в деревне', 2)

# h1.go_to(5)  # Вызов метода go_to
# h2.go_to(10)

print(h1)  # __str__
print(h2)  # __str__

print(len(h1))  # __len__
print(len(h2)) # __len__
