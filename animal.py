class Animal:
    def __init__(self, name: str, species: str, age: int):
        self.__name = name
        self.__species = species
        self.__age = age

    def __str__(self):
        return f'Animal "{self.__species.upper()}" (name: "{self.__name}", age: {self.__age})'

    def to_dict(self):
        return {
            "name": self.__name,
            "species": self.__species,
            "age": self.__age
        }