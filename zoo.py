from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper, Employee
from person import Person
from menu import Menu

class Zoo:
    __animals = [] # список тварин
    __enclosures = [] # список вол'єрів
    __employees = [] # список співробітників
    __zookeepers = [] # список персоналу, що відповідають за вол'єри

    # @property
    # def animals(self):
    #     return self.__animals
    @property
    def animals(self):
        str_list_animals = f'\n\t***\tLIST ANIMALS:\t***\n\n'
        if self.__animals:
            for index, [animal, enclosure] in enumerate(self.__animals):
                str_list_animals += f'\t{index + 1}. {animal}\t-\t{enclosure}\n'
        else:
            str_list_animals += f'\n\tNo data\n'

        return str_list_animals

    @animals.setter
    def animals(self, animal):
        self.__animals.append(animal)

    @property
    def enclosures(self):
        str_list_enclosures = f'\n\t***\tLIST ENCLOSURES:\t***\n'
        if self.__enclosures:
            for index, enclosure in enumerate(self.__enclosures):
                str_list_enclosures += f'\n\t{index + 1}. {enclosure}\n'
                if enclosure.animals:
                    for index_animal, animal in enumerate(enclosure.animals):
                        str_list_enclosures += f'\t\t{index_animal + 1}. {animal}\n'
                else:
                    str_list_enclosures += '\t\tThe list of animals is empty\n'
        else:
            str_list_enclosures += f'\n\tNo data\n'

        return str_list_enclosures

    @enclosures.setter
    def enclosures(self, enclosure):
        self.__enclosures.append(enclosure)

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, new_admin):
        self.__employees.append(new_admin)

    @property
    def zookeepers(self):
        return self.__zookeepers

    @zookeepers.setter
    def zookeepers(self, employee):
        self.__zookeepers.append(employee)

    def __str__(self):
        list_zoo_data = [self.__animals, self.__enclosures, self.__zookeepers, self.__employees]
        if not any(list_zoo_data):
            return f'No data'

# ************** Методи для меню ANIMALS

    def add_animal(self):
        new_animal = self.create_animal()
        self.place_animal_to_enclosure(new_animal)

    @staticmethod
    def create_animal():
        new_name = input("Enter name the animal: ")
        new_species = input("Enter species the animal: ")
        new_age = input("Enter age the animal: ")
        new_animal = Animal(new_name, new_species, int(new_age))
        # self.animals = new_animal
        return new_animal

    def place_animal_to_enclosure(self, animal):
        # поміщає тварину до вол'єру
        if not self.__enclosures:
            print('\nВол\'єри ще не заведені!!!\n')
            self.create_enclosure()

        enclosure = self.choose_enclosure()
        enclosure.animals = animal # додати тварину у список обраного вол'єру
        new_animal = [animal, enclosure]
        self.animals = new_animal # додати тварину у загальний список тварин
        print(f'{animal} place to enclosure "{enclosure}"')


    def choose_enclosure(self):
        Menu.display_list('LIST ENCLOSURES: ', self.__enclosures)
        choice = Menu.get_user_choice(len(self.__enclosures))
        return self.__enclosures[choice - 1]

    # ************** Методи для меню ENCLOSURES

    def create_enclosure(self):
        enclosure_id = len(self.__enclosures) + 1
        size = input("Enter a size of the enclosures: ")
        enclosure = Enclosure(enclosure_id, size)
        print(f'\nAdded new enclosure\n\tid: {enclosure.enclosure_id}, size: {size}')
        self.enclosures = enclosure # Додати вол'єр у список вол'єрів
        input('\nPress any key to continue ')

    def list_enclosures(self):
        if self.__enclosures:
            list_enclosures = []
            for enclosure in self.enclosures:
                animals = ''
                if enclosure.animals:
                    for index, animal in enumerate(enclosure.animals):
                        animals += f'{' ' * 45}{index +1}. {animal}\n'
                else:
                    print('No data')
                list_enclosures.append(f'{enclosure}:\n{animals}')
            Menu.display_list("LIST ENCLOSURE:", list_enclosures)
        else:
            print('List enclosures: No data\n')

    # ************** Методи для меню PERSONS

    def add_employee(self):
        employee = Employee()
        self.employees = employee

    def list_employees(self):
        Menu.display_list('List employees', self.employees)

    # def list_persons(self):
    #     print(Person.list_persons)
    def add_enclosure_to_zookeeper(self):
        choice_employee = None
        choice_enclosure = None
        if self.__employees:
            Menu.display_list('List employees:', self.__employees)
            choice = Menu.get_user_choice(len(self.__employees))
            choice_employee = self.__employees[choice - 1]
            print(f'Your choice: {choice_employee}')
            input('Press any key ')
        else:
            print('The list of employees is empty')
            input('Press any key ')
            return
        if self.__enclosures:

            choice_enclosure = self.choose_enclosure()
            print(f'Your choice: {choice_enclosure}')
            input('Press any key ')
        else:
            print("The list of enclosures is empty")
            input('Press any key ')
            return
        self.place_enclosure_to_employee(choice_employee, choice_enclosure)

    def place_enclosure_to_employee(self, employee, enclosure):
        # Перевірка, чи існує співробітник у списку __zookeepers
        if self.__zookeepers:
            for zookeeper, enclosures in self.__zookeepers:
                if employee == zookeeper:
                    print(f'Employee {employee} is in the list ')
                    print(f'list enclosures: {enclosures}')
                else:
                    self.__zookeepers.append(employee)
        else:
            print('list is empty')


        zookeeper = Zookeeper(employee, enclosure)

    def list_zookeepers(self):
        # if self.__zookeepers:
            # for employee in self.__zookeepers:
        Menu.display_list('List zookeeper:', self.__zookeepers)
