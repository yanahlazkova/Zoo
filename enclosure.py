class Enclosure:
    # Вольєр з атрибутами enclosure_id, title, size, animals (список тварин, які знаходяться у вольєрі)
    def __init__(self, enclosure_id, title, size):
        self.__enclosure_id = 'v001-' + str(enclosure_id)
        self.__title = title
        self.__size = size
        self.__animals = []

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, new_animal):
        self.__animals.append(new_animal)

    @property
    def enclosure_id(self):
        return self.__enclosure_id

    @property
    def title(self):
        return self.__title

    @property
    def size(self):
        return self.__size

    def to_dict(self):
        return {
            "enclosure_id": self.__enclosure_id,
            "size": self.__size
        }

    def __str__(self):
        return f"Вол'єр {self.__title} (id-{self.__enclosure_id} size-{self.__size})"
