class Person:
    __list_persons = []
    def __init__(self, name, employee_id):
        self.__name= name
        self.__employee_id = employee_id + str(f'-{len(self.__list_persons) + 1}')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def list_persons(self):
        return self.__list_persons

    @classmethod
    def add_person_to_list(cls, person):
        cls.__list_persons.append(person)

    @classmethod
    def get_list_persons(cls):
        return cls.__list_persons