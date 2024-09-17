class Enclosure:
    # Вольєр з атрибутами enclosure_id, size, animals (список тварин, які знаходяться у вольєрі)
    def __init__(self, enclosure_id, size):
        self.__enclosure_id = 'v001-' + str(enclosure_id)
        self.__size = size
        self.__animals = []

    @property
    def animals(self):
        return (animal for animal in self.__animals)

    @animals.setter
    def animals(self, new_animal):
        self.__animals.append(new_animal)

    def __str__(self):
        str_list_animals = '\nList animals:\n'
        if self.__animals:
            for animal in self.__animals:
                str_list_animals += f'\t- {animal}\n'
            else:
                str_list_animals += 'No data\n'
        else:
            str_list_animals += 'No data\n'
        return f"Вол'єр id-{self.__enclosure_id} size-{self.__size}\n{str_list_animals}"
