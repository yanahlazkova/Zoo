from menu import *
from myzoo import MyZoo

item_menu_animal = [
    'Add animal to enclosure',
    'Delete animal',
    'Move the animal into the enclosure',
    'List animals'
]
# menu_animal = SubMenu('MENU ANIMAL', item_menu_animal)

item_menu_enclosure = [
    'Add enclosure',
    'Delete enclosure',
    'Move the animal into the enclosure',
    'List enclosure'
]

item_menu_employees = [
    'Add employee',
    'List employees',
    'Delete employee',
    'Add enclosure to zookeeper',
    'Remove the zookeeper\'s enclosure',
    'List zookeepers',
]

data_zoo = MyZoo()

list_main_menu = [
    'Data zoo',
    'Animals',
    'Enclosures',
    'Employees',
    'Save to file'
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
                data_zoo.delete_animal()
            case 3:
                # Move the animal into the enclosure
                data_zoo.move_animal_into_enclosure()
            case 4:
                print(data_zoo.list_animals())
                input('Press eny key to continue ')
            case 5:
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
                data_zoo.delete_enclosure()
                input('Press eny key to continue ')
            case 3:
                data_zoo.move_animal_into_enclosure()
            case 4:
                print(data_zoo.list_enclosures())
                input('Press eny key to continue ')
            case 5:
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
                data_zoo.delete_employee()
                input('Press eny key to continue ')
            case 4:
                data_zoo.assign_enclosure_to_zookeeper()
            case 5:
                # Delete zookeeper
                data_zoo.remove_zookeeper_enclosure()
                input('Press eny key to continue ')
            case 6:
                print(data_zoo.list_zookeepers())
                input('Press eny key to continue ')
            case 7:
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
                data_zoo.save_to_file()
                input('Press any key to continue')
            case 6:
                exit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
