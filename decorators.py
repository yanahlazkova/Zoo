def check_entered_data(func):
    checked_data = []

    def wrapper(self, *args):
        for arg in args:
            while True:
                elem = input(arg)
                if elem:
                    checked_data.append(elem)
                    break
                else:
                    print('Данні повинні бути заповнені')
        data = func(checked_data)
        return data
    return wrapper

# @check_entered_data
# def create_obj_animal(new_name, new_species, new_age):
#     pass
#
# new_name = ["Enter name the animal: ", str]
# new_species = ["Enter species the animal: ", str]
# new_age = ["Enter age the animal: ", int]
# create_obj_animal(new_name, new_species, new_age)


class Descriptor:
    def __init__(self, list_data=None):
        if list_data is None:
            list_data = []
        self.list_data = list_data

    def __get__(self, instance, owner):
        return self.list_data
        # return instance.__dict__[self.list_name]

    def __set__(self, instance, value):
        print('method set')
        self.list_data.append(value)

    def __set_name__(self, owner, name):
        self.list_name = name
        print('self.list_name: ', name)
