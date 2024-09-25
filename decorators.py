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
