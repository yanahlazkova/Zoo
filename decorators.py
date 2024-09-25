class Descriptor:
    def __init__(self, list_data=None):
        if list_data is None:
            list_data = []
        self.list_data = list_data

    def __get__(self, instance, owner):
        return self.list_data

    def __set__(self, instance, value):
        self.list_data.append(value)
