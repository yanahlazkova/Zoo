from animal import Animal
from decorators import Descriptor
from enclosure import Enclosure
from menu import Menu


def check_list_empty(func):
    def check(*args):
        list_check = func(*args)
        if list_check:
            # func(*args)
            return print(list_check)
        else:
            print('List is empty')
    return check

class MyZoo:
    __animals = Descriptor()  # список тварин
    __enclosures = Descriptor()  # список вол'єрів
    __employees = Descriptor()  # список співробітників
    __zookeepers = Descriptor()  # список персоналу, що відповідають за вол'єри


    def __str__(self):
        lists_data_zoo = ''

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ANIMALS ***\n\n'
        if self.__animals:
            for index, animal in enumerate(self.__animals):
                lists_data_zoo += f'{index + 1}. {animal[0]} - {animal[1]}\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ENCLOSURES ***\n\n'
        if self.__enclosures:
            for index, enclosures in enumerate(self.__animals):
                lists_data_zoo += f'{index + 1}. {enclosures[0]} - {enclosures[1]}\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST EMPLOYEES ***\n\n'
        if self.__employees:
            pass
        else:
            lists_data_zoo += 'List is empty\n\n'
        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ZOOKEEPERS ***\n\n'
        if self.__zookeepers:
            pass
        else:
            lists_data_zoo += 'List is empty\n\n'

        return lists_data_zoo

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, animal):
        self.__animals = animal

    @property
    def enclosures(self):
        return self.__enclosures

    @enclosures.setter
    def enclosures(self, enclosure):
        self.__enclosures.append(enclosure)

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employee):
        self.__employees.append(employee)

    @property
    def zookeepers(self):
        return self.__zookeepers

    @zookeepers.setter
    def zookeepers(self, zookeeper):
        self.__zookeepers.append(zookeeper)

    def add_animal(self):
        new_name = input("Enter name the animal: ")
        new_species = input("Enter species the animal: ")
        new_age = input("Enter age the animal: ")
        new_animal = Animal(new_name, new_species, int(new_age))
        print('проверка списка:', len(self.__enclosures))
        self.place_animal_to_enclosure(new_animal)

    def place_animal_to_enclosure(self, animal):
        # поміщає тварину до вол'єру
        if not self.__enclosures:
            print('\nВол\'єри ще не заведені!!!\n')
            self.create_enclosure()

        enclosure = self.choose_item(self.__enclosures)
        enclosure.animals = animal # додати тварину у список обраного вол'єру
        new_animal = [animal, enclosure]
        self.animals = new_animal # додати тварину у загальний список тварин
        print(f'{animal} place to enclosure "{enclosure}"')

    def choose_item(self, list_items):
        Menu.display_list('LIST ENCLOSURES: ', list_items)
        choice = Menu.get_user_choice(len(list_items))
        return list_items[choice - 1]


    def create_enclosure(self):
        enclosure_id = len(self.__enclosures) + 1
        size = input("Enter a size of the enclosures: ")
        enclosure = Enclosure(enclosure_id, size)
        print(f'\nAdded new enclosure\n\tid: {enclosure.enclosure_id}, size: {size}')
        self.__enclosures = enclosure # Додати вол'єр у список вол'єрів
        input('\nPress any key to continue ')

