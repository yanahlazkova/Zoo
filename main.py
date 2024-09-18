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
    'enclosure_id',
    'size',
    'animals'
]

# menu_enclosure = Menu('MENU ENCLOSURE', item_menu_enclosure)

item_menu_zookeeper = [
    'name',
    'employee_id',
    'assigned_enclosures'
]

# menu_zookeeper = Menu('MENU ENCLOSURE', item_menu_zookeeper)

data_zoo = Zoo()

list_main_menu = [
    'Data zoo',
    'Animal',
    'Enclosure',
    'Zookeeper',
]

# main_menu = Menu('MAIN MENU:', list_main_menu)

def start_menu():
    # global list_main_menu
    while True:
        # main_menu.display_menu()
        Menu.display_menu('MAIN MENU', list_main_menu)
        choice_item_menu = Menu.get_user_choice(len(list_main_menu) + 1)
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
        Menu.display_menu('MENU ANIMALS:', item_menu_animal)
        choice_menu = Menu.get_user_choice(len(item_menu_animal) + 1)
        match choice_menu:
            case 1:
                print('Add new animal')
                data_zoo.add_animal()
            case 4:
                break


if __name__ == '__main__':
    start_menu()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
