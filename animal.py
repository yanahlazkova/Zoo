class Animal:
    def __init__(self, name: str, species: str, age: int):
        self.__name = name
        self.__species = species
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f'Animal "{self.__species.upper()}" (name: "{self.__name}", age: {self.__age})'

    def __eq__(self, other):
        return self.__name == other.name and self.__age == other.age and self.__species == other.species


    def to_dict(self):
        return {
            "name": self.__name,
            "species": self.__species,
            "age": self.__age
        }