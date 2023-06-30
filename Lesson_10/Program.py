#  Создайте три или более отдельных классов животных
#  У каждого класса должны быть как общие свойства. так и специфические для класса
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса

#  Вынесите общие свойства и методы классов в класс Животное
#  остальные классы наследуйте от него
#  Убедитесь, что в созданные ранее классы внесены правки

# 1.	Доработаем задачи 5-6. Создайте класс-фабрику.
# o	Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# o	Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 2.	Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
from decimal import Decimal


class Animal:
    def __init__ (self,name:str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'

class Bird(Animal):
    def __init__(self, name:str, weight: int, age: int, bird_type: str, sound:str):
        super().__init__(name,weight,age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.bird_type} '


class Dog(Animal):
    def __init__(self, name:str, weight: int, age: int, dog_type: str):
        super().__init__(name,weight,age)
        self.dog_type = dog_type

    def move(self):
        return  "Run"

    def say(self):
        return  "Gov"

    def __str__(self):
        return f'{super().__str__()} {self.dog_type} '

class Fish(Animal):
    def __init__(self, name:str, weight: int, age: int, fish_type: str):
        super().__init__(name,weight,age)
        self.fish_type = fish_type

    def move(self):
        return  "Swim"

    def say(selfs):
        return  ""

    def __str__(self):
        return f'{super().__str__()} {self.fish_type}'

class EnemyFactory:     # создаем класс Фабрика
    @staticmethod

    def build_sequence(self):
        return []

    def create_enemy(self,enemy_type):
        if enemy_type == "bird":
            return Bird("Glasha",10,4,"Soroka","Gru-gru")

        elif enemy_type ==  "dog":
            return Dog("Rex",10,5,"Barbos")

        elif enemy_type == "fish":
            return Fish("Gold",5,5,"Yantarnaya_s_perzem")

        else:
            raise ValueError ("Неверный тип животного")

    def build_number(self, string):
        return Decimal(string)

class Loader():        # Загрузчик для фабрики
    def load(string, factory):
        sequence = factory.create_enemy("fish")
        return sequence


f = EnemyFactory()
result = Loader.load("",f)
print(result)


if __name__  == '__main__':
    #dog = Dog ("Rex", 40,5, "Taks")
    #bird = Bird ("Gosha",1,3,"Popygay", "gru-gru")
    #fish = Fish ("Karp", 10,5, "River")

    #print(dog)
    #print(bird)
    #print(fish)
    pass