def check_entered_data(func):

    def wrapper(self, *args):
        checked_data = []
        for arg in args:
            while True:
                elem = input(arg)
                if elem:
                    checked_data.append(elem)
                    break
                else:
                    print('Данні повинні бути заповнені')
        data = func(self, checked_data)
        return data
    return wrapper


class Descriptor:
    def __init__(self, list_data=None):
        if list_data is None:
            list_data = []
        self.list_data = list_data

    def __get__(self, instance, owner):
        return self.list_data

    def __set__(self, instance, value):
        self.list_data.append(value)

    def __set_name__(self, owner, name):
        self.list_name = name
        print('self.list_name: ', name)

    def delete_value(self, value):
        if value in self.list_data:
            self.list_data.remove(value)
            print(f"'{value}' видалено зі списку {self.list_name}")
        else:
            print(f"'{value}' не знайдено у списку {self.list_name}")
