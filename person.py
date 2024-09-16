class Person:
    def __init__(self, name, employee_id):
        self.__name= name
        self.__employee_id = employee_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name



