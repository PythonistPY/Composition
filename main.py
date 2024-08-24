class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        return f"{self.name} Кушаю."

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} says chirp chirp!"

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} says roar!"

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        return f"{self.name} says hiss!"

# Функция полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} the {animal.__class__.__name__}")

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name} the {staff.__class__.__name__}")

# Класс для сотрудников
class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}."

class Veterinarian(Staff):
    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}."

# Пример использования
if __name__ == "__main__":
    # Создаем животных
    parrot = Bird(name="Polly", age=3, wing_span=30)
    lion = Mammal(name="Leo", age=5, fur_color="golden")
    snake = Reptile(name="Slippy", age=2, scale_color="green")

    # Создаем сотрудников
    keeper = ZooKeeper(name="John")
    vet = Veterinarian(name="Dr. Smith")

    # Создаем зоопарк
    zoo = Zoo()
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Показываем информацию о животных и сотрудниках
    print("Animals in the zoo:")
    zoo.show_animals()

    print("\nStaff in the zoo:")
    zoo.show_staff()

    # Демонстрируем полиморфизм
    print("\nAnimal sounds:")
    animal_sound(zoo.animals)

    # Демонстрируем работу сотрудников
    print("\nZoo Keeper action:")
    print(keeper.feed_animal(lion))

    print("\nVeterinarian action:")
    print(vet.heal_animal(snake))




