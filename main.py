from menu import *
from animal import Animal
from enclosure import Enclosure
from myzoo import MyZoo
from zookeeper import Zookeeper, Employee
from zoo import Zoo

item_menu_animal = [
    'Add animal to enclosure',
    'Delete animal without enclosure',
    'List animals'
]
# menu_animal = SubMenu('MENU ANIMAL', item_menu_animal)

item_menu_enclosure = [
    'Add enclosure',
    'Delete enclosure',
    'List enclosure'
]

item_menu_employees = [
    'Add employee',
    'List employees',
    'Add zookeeper',
    'List zookeepers',
]

data_zoo = MyZoo()

list_main_menu = [
    'Data zoo',
    'Animals',
    'Enclosures',
    'Employees',
]

def go_to_menu_animals():
    while True:
        Menu.display_menu('MENU ANIMALS:', item_menu_animal)
        choice_menu = Menu.get_user_choice(len(item_menu_animal) + 1)
        match choice_menu:
            case 1:
                # print('Add new animal')
                data_zoo.add_animal()
            case 2:
                pass
            case 3:
                print(data_zoo.list_animals())
                input('Press eny key to continue ')

            case 4:
                break


def go_to_menu_enclosures():
    while True:
        Menu.display_menu('MENU ENCLOSURES:', item_menu_enclosure)
        choice_menu = Menu.get_user_choice(len(item_menu_enclosure) + 1)
        match choice_menu:
            case 1:
                data_zoo.add_enclosure()
                input('Press eny key to continue ')
            case 2:
                print('Delete')
                input('Press eny key to continue ')
            case 3:
                print(data_zoo.list_enclosures())
                input('Press eny key to continue ')
            case 4:
                break


def go_to_menu_employee():
    while True:
        Menu.display_menu('MENU PERSONS', item_menu_employees)
        choice_menu = Menu.get_user_choice(len(item_menu_employees) + 1)
        match choice_menu:
            case 1:
                data_zoo.add_employee()
            case 2:
                print(data_zoo.list_employees())
                input('Press eny key to continue ')
            case 3:
                data_zoo.add_enclosure_to_zookeeper()
            case 4:
                print(data_zoo.list_zookeepers())
                input('Press eny key to continue ')
            case 5:
                break



if __name__ == '__main__':

    while True:
        Menu.display_menu('MAIN MENU', list_main_menu)
        choice_item_menu = Menu.get_user_choice(len(list_main_menu) + 1)
        match choice_item_menu:
            case 1:
                print(data_zoo)
                input('Press any key to continue')
            case 2:
                go_to_menu_animals()
            case 3:
                go_to_menu_enclosures()
            case 4:
                go_to_menu_employee()
            case 5:
                exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
