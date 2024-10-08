# Домашнее задание по теме "Зачем нужно наследование"
# import sys
class Livable:
    def __init__(self, name='Liveable'):
        self.name = name
        # self.edible = True


class Plant(Livable):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Animal(Livable):
    # не все животные - млекопитающие
    def __init__(self, name):
        super().__init__(name)
        self.fed = False
        self.alive = True

    # def feed(self, is_fed: bool, food):
    #     if is_fed:
    #         self.fed = True
    #         self.alive = True
    #         food.alive = False
    #         print(f'{self.name} съел {food.name} и насытился')
    #     else:
    #         self.fed = False
    #         self.alive = False
    #         print(f'{self.name} не смог съесть {food.name} и умер')

    def eat(self, food):
        if food.edible:
            self.fed = True
            self.alive = True
            print(f'{self.name} съел {food.name}')
        else:
            self.fed = False
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    # родительский класс для хищников и травоядных
    def __init__(self, name):
        super().__init__(name)

    # def feed(self, is_fed: bool, food):
    #     super().feed(is_fed, food)


class Predator(Mammal):
    # хищники, такие как волки и лисы - тоже млекопитающие
    def __init__(self, name):
        super().__init__(name)

    # def eat(self, food):
    #     food_is_edible = False
    #     for prey in food.__class__.mro():
    #         # хищники едят всех млекопитающих, в т.ч. и других хищников
    #         if prey.__name__.upper() == 'MAMMAL':
    #             food_is_edible = True
    #             break
    #     if food_is_edible:
    #         super().feed(True, food)
    #     else:
    #         super().feed(False, food)


class Herbivore(Mammal):
    # и травоядные - млекопитающие
    # def eat(self, food):  # Plant):
    #     if food.edible:
    #         super().feed(True, food)
    #     else:
    #         super().feed(False, food)
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# wolf = Predator('Серый Волк')
# fox = Predator('Братец Лис')
# goat = Herbivore('Козлик - недорослик')
# rabbit = Herbivore('Братец Кролик')
# bull = Herbivore('Бычок - смоляной бочок')
# flower = Flower('Борщевик ужасный')
# orange = Fruit('Сочный апельсин')
# carrot = Fruit('Красная морковка')
#
# print(wolf.name)
# print(fox.name)
# print(goat.name)
# print(rabbit.name)
# print(flower.name)
# print(orange.name)
# print(carrot.name)
#
# goat.eat(orange)
# print(wolf.alive)
# print(wolf.fed)
# print(goat.alive)
# print(goat.fed)
#
# wolf.eat(goat)
# print(wolf.fed)
# print(goat.alive)
#
# rabbit.eat(carrot)
# print(rabbit.fed)
#
# fox.eat(rabbit)
# print(fox.fed)
# print(rabbit.alive)
#
# wolf.eat(fox)
# print(wolf.fed)
# print(fox.alive)
#
# bull.eat(orange)
# print(bull.fed)
# print(bull.alive)
#
# bull.eat(flower)
# print(bull.fed)
# print(bull.alive)
#
# wolf.eat(flower)
# print(wolf.fed)
# print(wolf.alive)
