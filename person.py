from decorators import check_entered_data


class Person:
    __count_persons = 0

    def __init__(self, employee_id, name):
        # name = input('Enter the name: ')
        self.__name = name
        Person.__count_persons += 1
        self.__employee_id = employee_id + str(self.__count_persons)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, new_employee_id):
        self.__employee_id = new_employee_id

    @property
    def count_persons(self):
        return Person.__count_persons
