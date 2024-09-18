from animal import Animal
from enclosure import Enclosure
from menu import Menu
class Zoo:
    __animals = [] # список тварин
    __administrations = [] # список співробітників адміністрації
    __enclosures = [] # список вол'єрів
    __zookeeper = [] # список персоналу, що опікуються тваринами

    def __str__(self):
        list_zoo_data = [self.__animals, self.__enclosures, self.__zookeeper, self.__administrations]
        if not any(list_zoo_data):
            return f'No data'
        else:
            str_zoo_data = ''
            if self.__animals:
                str_zoo_data += '\nAnimals:\n'
                for animal in self.__animals:
                    str_zoo_data += f' - {animal}\n'
            else:
                str_zoo_data += '\nAnimals: No data\n'
            if self.__enclosures:
                str_zoo_data += f'\nEnclosures:\n'
                for enclosure in self.__enclosures:
                    str_zoo_data += f' - {enclosure}\n'
                    if enclosure.animals:
                        str_zoo_data += Zoo.__animals
                        # str_zoo_data += '\t\tList animals in enclosure:\n'
                        # for index, animal in enumerate(enclosure.animals):
                        #     str_zoo_data += f'\t{index + 1}. {animal}\n'
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

    def add_animal(self):
        new_animal = self.create_animal()
        enclosure = self.place_to_enclosure(new_animal)

    def create_animal(self):
        new_name = input("Enter name the animal: ")
        new_species = input("Enter species the animal: ")
        new_age = input("Enter age the animal: ")
        new_animal = Animal(new_name, new_species, new_age)
        self.__animals.append(new_animal)
        return new_animal

    def place_to_enclosure(self, animal):
        # поміщає тварину до вол'єру
        if not self.__enclosures:
            print('\nВол\'єри ще не заведені!!!\n')
            self.create_enclosure()

        enclosure = self.choose_enclosure()
        enclosure.animals = animal
        print(f'{animal} place to enclosure "{enclosure}"')

    def create_enclosure(self):
        enclosure_id = len(self.__enclosures) + 1
        size = input("Enter a size of the enclosures: ")
        enclosure = Enclosure(enclosure_id, size)
        print(f'\nAdded new enclosure\n\tid: {enclosure.enclosure_id}, size: {size}')
        self.__enclosures.append(enclosure)
        input('\nPress any key to continue ')

    def choose_enclosure(self):
        Menu.display_list('LIST ENCLOSURES: ', self.__enclosures)
        choice = Menu.get_user_choice(len(self.__enclosures))
        # if 1 <= choice <= len(self.__enclosures):
        return self.__enclosures[choice - 1]

    @property
    def animals(self):
        list_animals = ''
        list_animals += '\t\tList animals:\n'
        for index, animal in enumerate(self.__animals):
            list_animals += f'\t{index + 1}. {animal}\n'
        return list_animals

    @animals.setter
    def animals(self, animal):
        self.__animals.append(animal)

    @property
    def enclosures(self):
        return (enclosure for enclosure in self.__enclosures)

    # @enclosures.setter
    # def enclosures(self, enclosure):
    #     self.__enclosures.append(enclosure)
