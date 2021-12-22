from typing import DefaultDict, Dict, List, Callable
import click
import random

#1
class Margarita:
    """ Класс для пиицы Маргарита"""

    def __init__(self, size: str):
        self.name = 'Margarita' + '\U0001F9C0'
        self.recepie = ['tomatoe souce', 'mozarella', 'tomatoes']
        if size not in ['L', 'XL']:
            raise ValueError('Мы не делаем пиццу такого размера, выберите опцию: L, XL')
        else:
            self.size = size

        #если пицца XL - добавялем в два раза больше ингредиентов
        if size =='XL':
            new_recepie = []
            for ingredient in self.recepie:
                ingredient = ingredient + ' x2'
                new_recepie.append(ingredient)
            self.recepie = new_recepie

    def dict(self):
        """  Вывод рецепта в виде словаря """
        return {self.name: self.recepie}

    def __eq__(self, other):
        return self.recepie == other.recepie

class Peperonie:
    """ Класс для пиицы Пеперони"""

    def __init__(self, size: str):
        self.name = 'Peperonie' + '\U0001F355'
        self.recepie = ['tomatoe souce', 'mozarella', 'peperonie']
        if size not in ['L', 'XL']:
            raise ValueError('Мы не делаем пиццу такого размера, выберите опцию: L, XL')
        else:
            self.size = size

        #если пицца XL - добавялем в два раза больше ингредиентов
        if size =='XL':
            new_recepie = []
            for ingredient in self.recepie:
                ingredient = ingredient + ' x2'
                new_recepie.append(ingredient)
            self.recepie = new_recepie

    def dict(self):
        """  Вывод рецепта в виде словаря """
        return {self.name: self.recepie}

    def __eq__(self, other):
        return self.recepie == other.recepie

class Hawaii:
    """ Класс для Гавайской пиццы """

    def __init__(self, size: str):
        self.name = 'Hawaii' + '\U0001F34D'
        self.recepie = ['tomatoe souce', 'mozarella',
                        'chicken', 'pineapple']
        if size not in ['L', 'XL']:
            raise ValueError('Мы не делаем пиццу такого размера, выберите опцию: L, XL')
        else:
            self.size = size

        #если пицца XL - добавялем в два раза больше ингредиентов
        if size =='XL':
            new_recepie = []
            for ingredient in self.recepie:
                ingredient = ingredient + ' x2'
                new_recepie.append(ingredient)
            self.recepie = new_recepie

    def dict(self):
        """  Вывод рецепта в виде словаря """
        return {self.name: self.recepie}

    def __eq__(self, other):
        return self.recepie == other.recepie

# if __name__ == '__main__':
#     print(Margarita('XL').dict())
#     print(Peperonie('L').dict())
#     print(Hawaii('XL').dict())
#
#     print(Margarita('XL').recepie == Margarita('XL').recepie)
#     print(Margarita('L').recepie == Margarita('XL').recepie)
#     print(Peperonie('XL').recepie == Margarita('L').recepie)

# #1_2 - подумать
#
# class Pizza:
#
#     def __init__(self):
#
#     def __eg__(self):
#
#     def dict(self): # для преобразования данных для вывода

#2

import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
@click.option("--delivery", default=False, is_flag=True)
def order(pizza: str, size:str, delivery: bool):
    """Готовит и доставляет пиццу"""
    # pizza = pizza.upper().title()
    # size = size.upper()
    # if pizza== 'Peperonie':
    #     print(bake(Peperonie(size=size)))
    #     if delivery:
    #         print(delivery(Peperonie(size=size)))
    # elif pizza == 'Hawaii':
    #     print(bake(Hawaii(size=size)))
    #     if delivery:
    #         print(delivery(Hawaii(size=size)))
    # elif pizza == 'Margarita':
    #     print(bake(Margarita(size=size)))
    #     if delivery:
    #         print(delivery(Margarita(size=size)))


@cli.command()
def menu():
    """Меню"""
    print(" " *30, '\U0001F498' + "Меню" + '\U0001F498\n', end="") #заголовок
    pizzas_list = [Margarita('L'),
                   Margarita('XL'),
                   Peperonie('L'),
                   Peperonie('XL'),
                   Hawaii('L'),
                   Hawaii('XL')
                   ]
    for pizza in pizzas_list:
        print(f'{pizza.name} {pizza.size}:{pizza.recepie}')

# if __name__ == "__main__":
#     cli()
#3

def log(message: str):
    """Параметрический декоратор, выводит название процесса, название пиццы и время"""
    def decorator(func):
        def decorated(pizza):
            option_name = func(pizza)
            pizza_time = random.randint(5, 10)
            if func.__name__ == "bake" and pizza.size == "XL":
                pizza_time *= 2
            return message.format(option_name, pizza.name, pizza_time)
        return decorated
    return decorator

@log("{} {} за \U0001F31F {} мин!")
def bake(pizza) -> str:
    """Возвращает сообщение о готовой пиццы."""
    return "\U0001F31F Приготовили"


@log("{} {} за \U0001F31F {} мин!")
def delivery(pizza) -> str:
    """Возвращает сообщение о доставке пиццы."""
    return "\U0001F38A  Доставили"


@log("{} {} за \U0001F31F {} мин!")
def pickup(pizza) -> str:
    """Возвращает сообщение о самовывозе пиццы."""
    return "\U0001F3E1 Забрали"

# if __name__ == '__main__':
#     print(bake(Hawaii('XL')))
#     print(bake(Margarita('L')))
#     print(bake(Peperonie('XL')))

#4 Tests
# import unittest
# class TestTF(unittest.TestCase):
#
#     def test_dict(self):
#         """ Проверка верно выводящихся названия пиццы и ингредиентов"""
#         actual = Margarita('XL').dict()
#         expected = {'Margarita🧀': ['tomatoe souce x2', 'mozarella x2', 'tomatoes x2']}
#         self.assertEqual(actual, expected)
#
#     def test_recepie(self):
#         """ Проверка верно указанных рецептов"""
#         actual = Margarita('XL').recepie
#         expected = ['tomatoe souce x2', 'mozarella x2', 'tomatoes x2']
#         self.assertEqual(actual, expected)
#
#     def test_eql(self):
#         """Тест сравнения пицц """
#         first_pizza = Margarita('L').size
#         second_pizza = Margarita('L').size
#         self.assertTrue(first_pizza == second_pizza)
#
#     def test_non_eg(self):
#         """ Тест на сравнение пицц с разными размерами"""
#         first_pizza = Margarita('L').size
#         second_pizza = Margarita('XL').size
#         self.assertFalse(first_pizza == second_pizza)


# if __name__ == '__main__':
#     unittest.main()