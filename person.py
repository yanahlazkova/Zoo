class Person:
    __list_persons = []
    # __employee_id = 'pr00-'
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
    #     print(type(self.__list_persons))
    #     if self.__list_persons:
    #         return self.__list_persons
    #     else:
    #         return 'The list of persons is empty'
        return (person for person in self.__list_persons)

    @list_persons.setter
    def list_persons(self, person):
        self.__list_persons.append(person)

    @classmethod
    def add_person_to_list(cls, person):
        cls.__list_persons.append(person)
