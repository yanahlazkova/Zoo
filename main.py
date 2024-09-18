from menu import *
from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
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

item_menu_persons = [
    'Add administrator',
    'List administrations',
    'Add zookeeper',
    'List zookeepers',
    'List persons'
]

data_zoo = Zoo()

list_main_menu = [
    'Data zoo',
    'Animals',
    'Enclosures',
    'Persons',
]

# main_menu = Menu('MAIN MENU:', list_main_menu)


def start_menu():
    # global list_main_menu
    while True:
        Menu.display_menu('MAIN MENU', list_main_menu)
        choice_item_menu = Menu.get_user_choice(len(list_main_menu) + 1)
        match choice_item_menu:
            case 1:
                data_zoo.list_animals()
                data_zoo.list_enclosures()
                input('Press any key to continue')
            case 2:
                go_to_menu_animals()
            case 3:
                go_to_menu_enclosures()
            case 4:
                go_to_menu_persons()
            case 5:
                exit()


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
                data_zoo.list_animals()
                input('Press eny key to continue ')

            case 4:
                break


def go_to_menu_enclosures():
    while True:
        Menu.display_menu('MENU ENCLOSURES:', item_menu_enclosure)
        choice_menu = Menu.get_user_choice(len(item_menu_enclosure) + 1)
        match choice_menu:
            case 1:
                data_zoo.create_enclosure()
            case 3:
                data_zoo.list_enclosures()
                input('Press eny key to continue ')

            case 4:
                break


def go_to_menu_persons():
    while True:
        Menu.display_menu('MENU PERSONS', item_menu_persons)
        choice_menu = Menu.get_user_choice(len(item_menu_persons) + 1)
        match choice_menu:
            case 1:
                data_zoo.add_administrator()
            case 2:
                data_zoo.list_administrations()
                input('Press eny key to continue ')
            case 4:
                pass
            case 5:
                data_zoo.list_persons()
                input('Press eny key to continue ')
            case 6:
                break



if __name__ == '__main__':
    start_menu()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
