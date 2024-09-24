class Descriptor:
    def __init__(self, list_data=None):
        if list_data is None:
            list_data = []
        self.list_data = list_data

    def __get__(self, instance, owner):
        if self.list_data:
            # print(f'instance: {instance}, owner: {owner}')
            return self.list_data
        else:
            print()
            return 'List is empty'

    def __set__(self, instance, value):
        self.list_data.append(value)
