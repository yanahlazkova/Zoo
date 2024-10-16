from animal import Animal
from decorators import Descriptor, check_entered_data
from enclosure import Enclosure
from menu import Menu
from zookeeper import Employee, Zookeeper
import json


class MyZoo:
    __animals = Descriptor()  # список тварин
    __enclosures = Descriptor()  # список вол'єрів
    __employees = Descriptor()  # список співробітників
    __zookeepers = Descriptor()  # список персоналу, що відповідають за вол'єри

    def __init__(self, data_file='zoo_data1.json'):
        # Загружаем данные при инициализации
        self.load_from_file(data_file)

    def load_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)

                # Завантаження вол'єрів
                for enclosure_data in data['enclosures']:
                    id_enclosure = enclosure_data['enclosure_id'][enclosure_data['enclosure_id'].index('-') + 1:]
                    self.__enclosures = Enclosure(id_enclosure, enclosure_data['title'], enclosure_data['size'])

                # Завантаження тварин
                for animal_data in data['animals']:
                    new_animal = Animal(animal_data['name'], animal_data['species'], animal_data['age'])
                    enclosure_id = animal_data['enclosure']
                    new_enclosure = self.find_enclosure(enclosure_id)
                    self.__animals = [new_animal, new_enclosure]

                # додаємо тварин у список вол'єрів
                for enclosure_data in data['enclosures']:
                    enclosure = self.find_enclosure(enclosure_data['enclosure_id'])
                    for animal in enclosure_data['animals']:
                        enclosure.animals = self.find_animal(animal)


                # Завантаження співробітників
                for employee_data in data['employees']:
                    new_employee = Employee(employee_data['job_title'], employee_data['name'])
                    new_employee.employee_id = employee_data['employee_id']
                    self.__employees = new_employee

                # Завантажуємо наглядачів та зв'язуємо їх з вол'єрами
                for zookeeper_data in data['zookeepers']:
                    employee = self.find_employee(zookeeper_data['employee_id'])
                    if zookeeper_data['enclosures']:
                        # TODO: необхідно створити об'єкт наглядача
                        zookeeper = Zookeeper(employee, None)
                        for id_enclosure in zookeeper_data['enclosures']:
                            new_enclosure = self.find_enclosure(id_enclosure)
                            zookeeper.list_enclosures = new_enclosure
                    self.__zookeepers = zookeeper
            print("Данные успешно загружены.")

        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")

    def find_animal(self, animal):
        for object_animal, enclosure in self.__animals:
            if object_animal == animal:
                return object_animal
        return None

    def find_employee(self, employee_id):
        for employee in self.__employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def find_enclosure(self, id_enclosure):
        for enclosure in self.__enclosures:
            if enclosure.enclosure_id == id_enclosure:
                return enclosure
        return None

    def __str__(self):
        lists_data_zoo = ''

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ANIMALS ***\n\n'
        if self.__animals:
            for index, [animal, enclosures] in enumerate(self.__animals):
                lists_data_zoo += f'{index + 1}. {animal} - {enclosures}\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ENCLOSURES ***\n\n'
        if self.__enclosures:
            for index, enclosures in enumerate(self.__enclosures):
                lists_data_zoo += f'{index + 1}. {enclosures}:\n'
                if enclosures.animals:
                    for index, animal in enumerate(enclosures.animals):
                        lists_data_zoo += f'\t\t{index +1}. {animal}\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST EMPLOYEES ***\n\n'
        if self.__employees:
            for index, employee in enumerate(self.__employees):
                lists_data_zoo += f'{index + 1}. {employee}\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ZOOKEEPERS ***\n\n'
        if self.__zookeepers:
            for index, zookeeper in enumerate(self.__zookeepers):
                lists_data_zoo += f'{index + 1}. {zookeeper.zookeeper}:\n'
                if zookeeper.list_enclosures:
                    for index, enclosure in enumerate(zookeeper.list_enclosures):
                        lists_data_zoo += f'\t\t{index + 1}. {enclosure}\n'
                else:
                    lists_data_zoo += f'\t\tList of the enclosures is empty\n'
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
        # self.__enclosures.append(enclosure)
        self.__enclosures = enclosure
    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employee):
        # self.__employees.append(employee)
        self.__employees = employee

    @property
    def zookeepers(self):
        return self.__zookeepers

    @zookeepers.setter
    def zookeepers(self, zookeeper):
        # self.__zookeepers.append(zookeeper)
        self.__zookeepers = zookeeper

    def add_animal(self):
        new_name = "Enter name the animal: "
        new_species = "Enter species the animal: "
        new_age = "Enter age the animal: "
        new_animal = self.create_obj_animal(new_name, new_species, new_age)
        # print('проверка списка:', len(self.__enclosures))
        self.place_animal_to_enclosure(new_animal)

    @check_entered_data
    def create_obj_animal(self, new_data):
        new_animal = Animal(*new_data)
        print('new_animal: ', new_animal)
        return new_animal

    def place_animal_to_enclosure(self, animal):
        # поміщає тварину до вол'єру
        if not self.__enclosures:
            print('\nВол\'єри ще не заведені!!!\n')
            self.add_enclosure()

        enclosure = self.choose_item(self.__enclosures)
        enclosure.animals = animal # додати тварину у список обраного вол'єру
        new_animal = [animal, enclosure]
        self.animals = new_animal # додати тварину у загальний список тварин
        print(f'{animal} place to enclosure "{enclosure}"')

    def move_animal_into_enclosure(self):
        # переміщення тварини у інший вол'єр
        if len(self.__enclosures) <= 1:
            print('Список вол\'єрів пустий, немає куди переміщати')
            input('Press any key ')
            return
        if self.__animals:
            # вибір травини
            print(self.list_animals())
            choice_item_animal = Menu.get_user_choice(len(self.__animals))
            choice_animal, current_enclosure = self.__animals[choice_item_animal - 1]
            # вибір вол'єра
            print((self.list_enclosures()))
            choice_item_enclosure = Menu.get_user_choice(len(self.__enclosures))
            choice_enclosure = self.__enclosures[choice_item_enclosure - 1]
            current_enclosure.animals.remove(choice_animal)
            current_enclosure = choice_enclosure
            self.__animals[choice_item_animal - 1][1] = choice_enclosure
            choice_enclosure.animals = choice_animal

            print(f'Animal {self.__animals[choice_item_animal - 1][0]} moved '
                  f'to enclosure {self.__animals[choice_item_animal - 1][1]}')
        else:
            print('List of animals is empty')
            input('Press any key to continue ')

    @staticmethod
    def choose_item(list_items):
        # display list enclosures and do choice
        Menu.display_list('LIST ENCLOSURES: ', list_items)
        choice = Menu.get_user_choice(len(list_items))
        return list_items[choice - 1]

    def list_animals(self):
        lists_animal = ''

        lists_animal += f'\n\n{' ' * 5}*** LIST ANIMALS ***\n\n'
        if self.__animals:
            for index, [animal, enclosures] in enumerate(self.__animals):
                lists_animal += f'{index + 1}. {animal} - {enclosures}\n'
        else:
            lists_animal += 'List is empty\n\n'
        return lists_animal

    def delete_animal(self):
        if self.__animals:
            print(self.list_animals())
            choice_item = Menu.get_user_choice(len(self.__animals))
            choice_animal = self.__animals[choice_item - 1]
            self.__animals.remove(choice_animal)
            enclosures = choice_animal[1]
            enclosures.animals.remove(choice_animal[0])
            # print(*enclosures.animals)
        else:
            print(f'List "ANIMALS" is empty')
            input("Press any key ")
        print(self.list_animals())


########## Методи роботи з даними eclosures #########

    def add_enclosure(self):
        size = "Enter a size of the enclosures: "
        title = "Enter a name of the enclosures: "
        new_enclosure = self.create_enclosure(title, size)

        print(f'\nAdded new enclosure "{new_enclosure.title}"\n\tid: {new_enclosure.enclosure_id}, size: {new_enclosure.size}')
        self.__enclosures = new_enclosure  # Додати вол'єр у список вол'єрів

    @check_entered_data
    def create_enclosure(self, new_data):
        enclosure_id = len(self.__enclosures) + 1
        new_data.insert(0, enclosure_id)
        enclosure = Enclosure(*new_data)
        return enclosure

    def list_enclosures(self):
        lists_enclosures = ''
        lists_enclosures += f'\n\n{' ' * 5}*** LIST ENCLOSURES ***\n\n'
        if self.__enclosures:
            for index, enclosures in enumerate(self.__enclosures):
                lists_enclosures += f'{index + 1}. {enclosures}:\n'
                if enclosures.animals:
                    for index, animal in enumerate(enclosures.animals):
                        lists_enclosures += f'\t\t{index + 1}. {animal}\n'
                else:
                    lists_enclosures += '\t\tList is empty\n\n'
        else:
            lists_enclosures += 'List is empty\n\n'
        return lists_enclosures

    def delete_enclosure(self):
        if self.__enclosures:
            print(self.list_enclosures())
            choice_item = Menu.get_user_choice(len(self.__enclosures))
            choice_enclosure = self.__enclosures[choice_item - 1]
            if choice_enclosure.animals:
                print('У вол\'єрі є тварини, перемістіть їх у інший вол\'єр і повторіть видалення знову' )
                return
            self.__enclosures.remove(choice_enclosure)
        else:
            print('Список вол\'єрів пустий')


########## Методи роботи з даними employees #########

    def add_employee(self):
        new_employee = 'Enter the job title: '
        new_name_person = 'Enter the name: '
        new_employee = self.create_employee(new_employee, new_name_person)

        print(f'\nAdded new employee:\n\t{new_employee}')
        self.__employees = new_employee  # Додати працівника у список працівників
        input('Press any key ')

    @check_entered_data
    def create_employee(self, new_employee):
        employee = Employee(*new_employee)
        return employee

    def list_employees(self):
        lists_employee = ''
        lists_employee += f'\n\n{' ' * 5}*** LIST EMPLOYEES ***\n\n'
        if self.__employees:
            for index, employee in enumerate(self.__employees):
                lists_employee += f'\t\t{index + 1}. {employee}\n'
        else:
            lists_employee += 'List is empty\n\n'
        return lists_employee

    def assign_enclosure_to_zookeeper(self):
        choice_employee = None
        choice_enclosure = None
        if self.__employees:
            Menu.display_list('LIST EMPLOYEES:', self.__employees)
            choice = Menu.get_user_choice(len(self.__employees))
            choice_employee = self.__employees[choice - 1]

        else:
            print('!!! The list of employees is empty')
            input('Press any key ')
            return

        if self.__enclosures:
            choice_enclosure = self.choose_item(self.__enclosures)

        else:
            print("!!! The list of enclosures is empty")
            input('Press any key ')
            return
        self.place_enclosure_into_employee(choice_employee, choice_enclosure)

    def place_enclosure_into_employee(self, employee, enclosure):
        found_employee = next((zookeeper for zookeeper in self.__zookeepers if zookeeper.zookeeper == employee), None)
        if found_employee:
            found_enclosure = next((item for item in found_employee.list_enclosures if item == enclosure), None)
            if found_enclosure:
                print(f'!!! Вол\'єр {enclosure} вже існує у списку')
                input('Press any key ')
                return
            else:
                found_employee.list_enclosures = enclosure
                print(f'Наглядачу {employee} додано вол\'єр {enclosure}')
            Menu.display_list('List of the enclosures', found_employee.list_enclosures)
            input('Press any key ')

        else:
            new_zookeeper = Zookeeper(employee, enclosure)
            self.__zookeepers = new_zookeeper
            print('Added new zookeeper into the list')
            Menu.display_list(employee.name, new_zookeeper.list_enclosures)
            input('Press any key ')

    def list_zookeepers(self):
        lists_data_zoo = ''
        lists_data_zoo += f'\n\n{' ' * 5}*** LIST ZOOKEEPERS ***\n\n'
        if self.__zookeepers:
            for index, zookeeper in enumerate(self.__zookeepers):
                lists_data_zoo += f'{index + 1}. {zookeeper.zookeeper}:\n'
                if zookeeper.list_enclosures:
                    for index, enclosure in enumerate(zookeeper.list_enclosures):
                        lists_data_zoo +=f'\t\t{index + 1}. {enclosure}\n'
                else:
                    lists_data_zoo +=f'\t\tList of the enclosures is empty\n'
        else:
            lists_data_zoo += 'List is empty\n\n'

        return lists_data_zoo

    def delete_employee(self):
        if self.__employees:
            Menu.display_list('LIST EMPLOYEES', self.__employees)
            choice = Menu.get_user_choice(len(self.__employees))
            choice_employee = self.__employees[choice - 1]
            print(f'\nYour choice: {choice_employee}\n')
            input('Press eny key to continue ')
            self.__employees.pop(choice - 1)
            print(f'\n{choice_employee}  DELETED\n')
        else:
            print('Список співробітників пустий.\n')

    def save_to_file(self):
        filename = "zoo_data1.json"
        animals_list = []

        for animal, enclosure in self.__animals:
            animal_dict = animal.to_dict()
            animal_dict['enclosure'] = enclosure.enclosure_id
            animals_list.append(animal_dict)


        data = {
            "animals": animals_list,
            "enclosures": [enclosure.to_dict() for enclosure in self.__enclosures],
            "employees": [employee.to_dict() for employee in self.__employees],
            "zookeepers": [zookeeper.to_dict() for zookeeper in self.__zookeepers]
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            
    def remove_zookeeper_enclosure(self):
        if self.__zookeepers:
            print(self.list_zookeepers())
            choice = Menu.get_user_choice(len(self.__zookeepers))
            choice_zookeeper = self.__zookeepers[choice - 1]
            print(f'\nYour choice: {choice_zookeeper.zookeeper}\n')
            list_enclosure = choice_zookeeper.list_enclosures
            Menu.display_list('List employer\'s enclosure:', list_enclosure)
            choice = Menu.get_user_choice(len(list_enclosure))
            choice_enclosure = list_enclosure[choice - 1]
            print(f'Your choice: {choice_enclosure}')
            input('Press eny key to continue ')
            choice_zookeeper.list_enclosures.pop(choice - 1)
            print(f'\n{choice_enclosure}  DELETED\n')
        else:
            print('Список наглядачів за вол\'єрами пустий.\n')

