# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

class Vehicle:
    __COLOR_VARIANTS = {'BLACK', 'RED', 'WHITE', 'YELLOW', 'BLUE'}

    def __init__(self, owner: str, model: str, color: str, power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_engine_power(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f'Модель: {self.__model},\nмощность двигателя: {self.__engine_power}л.с.,\nцвет: {self.__color}, '
              f'\nВладелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


v = Sedan('Bobby', 'Crysler Road master', 'Red', 250)
v.print_info()

v.set_color('Brown')
v.set_color('Black')
v.owner = 'Eddy'

v.print_info()
