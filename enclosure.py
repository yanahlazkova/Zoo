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

    @property
    def enclosure_id(self):
        return self.__enclosure_id

    def __str__(self):
        return f"Вол'єр id-{self.__enclosure_id} size-{self.__size}"
