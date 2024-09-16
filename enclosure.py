class Enclosure:
    # Вольєр з атрибутами enclosure_id, size, animals (список тварин, які знаходяться у вольєрі)
    def __init__(self, enclosure_id, size, animals: list):
        self.__enclosure_id = enclosure_id
        self.__size = size
        self.__animals = animals
        
    @property
    def animals(self):
        return (animal for animal in self.__animals)

    @animals.setter
    def animals(self, new_animal):
        return self.__animals.append(new_animal)
