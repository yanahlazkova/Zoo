class Animal:
    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age

    def __str__(self):
        return f'Animal {self.__species}:\tname: "{self.__name}", age: {self.__age}'
