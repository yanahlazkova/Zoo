from animal import Animal
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
                str_zoo_data += f'Animals:\n{list(self.__animals)}'
            else:
                str_zoo_data += 'Animals: No data'
            if self.__enclosures:
                str_zoo_data += f'Animals:\n{list(self.__enclosures)}'
            if self.__administrations:
                str_zoo_data += f'Animals:\n{list(self.__administrations)}'
            if self.__zookeeper:
                str_zoo_data += f'Animals:\n{list(self.__zookeeper)}'
        return f'Animals:\n{list(self.__animals)}'

    def add_animal(self):
        new_name = input("Enter name the animal: ")
        new_species = input("Enter species the animal: ")
        new_age = input("Enter age the animal: ")
        new_animal = Animal(new_name, new_species, new_age)
        self.__animals.append(new_animal)
        # self.__enclosures
