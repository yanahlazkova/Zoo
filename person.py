class Person:
    __list_persons = []
    # __employee_id = 'pr00-'
    def __init__(self, name, employee_id):
        self.__name= name
        self.__employee_id = employee_id + str(len(self.__list_persons))

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
        return (person for person in self.__list_persons)

    @list_persons.setter
    def list_persons(self, new_person):
        self.__list_persons.append(new_person)

