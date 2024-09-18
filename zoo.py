from animal import Animal
from enclosure import Enclosure
from menu import Menu
class Zoo:
    __animals = [] # список тварин
    __enclosures = [] # список вол'єрів
    __administrations = [] # список співробітників адміністрації
    __zookeeper = [] # список персоналу, що опікуються тваринами

    @property
    def animals(self):
        # list_animals = ''
        # list_animals += '\t\tList animals:\n'
        # for index, animal in enumerate(self.__animals):
        #     list_animals += f'\t{index + 1}. {animal[0]} - {animal[1]}\n'
        # return list_animals
        return (animal for animal in self.__animals)

    @animals.setter
    def animals(self, animal):
        self.__animals.append(animal)

    @property
    def enclosures(self):
        return (enclosure for enclosure in self.__enclosures)

    @enclosures.setter
    def enclosures(self, enclosure):
        self.__enclosures.append(enclosure)

    def __str__(self):
        list_zoo_data = [self.__animals, self.__enclosures, self.__zookeeper, self.__administrations]
        if not any(list_zoo_data):
            return f'No data'
        else:
            str_zoo_data = ''
            if self.__animals:
                str_zoo_data += '\nAnimals:\n'
                for index, animal in enumerate(self.animals):
                    str_zoo_data += f' - {animal}\n'
            else:
                str_zoo_data += '\nAnimals: No data\n'

            if self.__enclosures:
                str_zoo_data += f'\nEnclosures:\n'
                # for enclosure in self.__enclosures:
                for index, enclosure in enumerate(self.enclosures):
                    str_zoo_data += f' {index + 1}. {enclosure}\n'
                    if enclosure.animals:
                        # str_zoo_data += self.animals
                        str_zoo_data += enclosure.animals

                    else:
                        str_zoo_data += '\t\tЩе намає тварин'
            else:
                    str_zoo_data += '\nEnclosure: No data\n'
            if self.__administrations:
                str_zoo_data += f'\nAdministrations:\n'
                for administration in self.__administrations:
                    str_zoo_data += f' - {administration}\n'
            else:
                    str_zoo_data += '\nAdministrations: No data\n'
            if self.__administrations:
                str_zoo_data += f'\nZookeeper:\n'
                for zookeeper in self.__zookeeper:
                    str_zoo_data += f' - {zookeeper}\n'
            else:
                    str_zoo_data += '\nZookeeper: No data\n'

        return f'Zoo:\n{str_zoo_data}'


# ************** Методи для меню ANIMALS

    def add_animal(self):
        new_animal = self.create_animal()
        self.place_to_enclosure(new_animal)

    def create_animal(self):
        new_name = input("Enter name the animal: ")
        new_species = input("Enter species the animal: ")
        new_age = input("Enter age the animal: ")
        new_animal = Animal(new_name, new_species, int(new_age))
        # self.animals = new_animal
        return new_animal

    def place_to_enclosure(self, animal):
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
        # if 1 <= choice <= len(self.__enclosures):
        return self.__enclosures[choice - 1]

    def list_animals(self):
        if self.__animals:
            list_animals = []
            for animal, enclosure in self.__animals:
                list_animals.append(f'{animal}\t-\t{enclosure}')
            Menu.display_list('The List of animals', list_animals)
        else:
            print('List animals: No data\n')

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
