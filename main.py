from menu import *
from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
from zoo import Zoo

item_menu_animal = [
    'name',
    'species',
    'age'
]
menu_animal = Menu('MENU ANIMAL', item_menu_animal)

item_menu_enclosure = [
    'enclosure_id',
    'size',
    'animals'
]

menu_enclosure = Menu('MENU ENCLOSURE', item_menu_enclosure)

item_menu_zookeeper = [
    'name',
    'employee_id',
    'assigned_enclosures'
]

menu_zookeeper = Menu('MENU ENCLOSURE', item_menu_zookeeper)

data_zoo = Zoo()

list_main_menu = [
    {'menu_title': 'Data zoo', 'menu': data_zoo},
    {'menu_title': 'Animal', 'menu': menu_animal},
    {'menu_title': 'Enclosure', 'menu': menu_enclosure},
    {'menu_title': 'Zookeeper', 'menu': menu_zookeeper},
]
if __name__ == '__main__':
    main_menu = Menu('MAIN MENU:', list_main_menu)
    main_menu.display_menu()
    # choice_item_menu = main_menu.get_user_choice()
    # print(f'Your choice: {choice_item_menu}')
    while True:
        choice_item_menu = main_menu.get_user_choice()
        match choice_item_menu:
            case 1:
                print(data_zoo)
                input('Press any key to continue')
            case 5:
                exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
