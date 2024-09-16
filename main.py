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
menu_animal = SubMenu('MENU ANIMAL', item_menu_animal)

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

menu = Menu('MAIN MENU:', list_main_menu)

def main_menu():
    while True:
        menu.display_menu()
        choice_item_menu = menu.get_user_choice()
        match choice_item_menu:
            case 1:
                print(data_zoo)
                input('Press any key to continue')
            case 2:
                go_to_menu_animal()
                # menu_animal.display_menu_items()
                # input('Press any key to continue')

            case 5:
                exit()

def go_to_menu_animal():
    while True:
        menu_animal.display_menu()
        choice_menu = menu_animal.get_user_choice()
        match choice_menu:
            case 1:
                print('Add new animal')
            case 4:
                break

if __name__ == '__main__':
    main_menu()
    # choice_item_menu = main_menu.get_user_choice()
    # print(f'Your choice: {choice_item_menu}')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
