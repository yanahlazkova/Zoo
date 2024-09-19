from person import Person


class Administration(Person):
    __pref_id = 'ad-'

    def __init__(self):
        name = input('Enter the name: ')
        employee_id = self.__pref_id + str(len(Person.get_list_persons()) + 1)
        super().__init__(name, employee_id)
        # employee_id = input('Введіть префікс для id: ')
        self.__job_title = input('Enter the job title: ')
        Person.add_person_to_list(self)

    def __str__(self):
        return f'{self.__job_title}\t-\tid: {self.employee_id}, name: {self.name}'


class Zookeeper(Person):
    __pref_id = 'ad-'
    def __init__(self, name, assigned_enclosures: list):
        employee_id = self.__pref_id + str(len(Person.get_list_persons()) + 1)
        super().__init__(name, employee_id)
        self.__assigned_enclosures = assigned_enclosures # list of enclosures

    def __str__(self):
        return f'Zookeeper\t-\tid: {self.employee_id}, {self.name}, '

    @property
    def assigned_enclosures(self):
        return self.__assigned_enclosures

    @assigned_enclosures.setter
    def assigned_enclosures(self, animal):
        self.__assigned_enclosures.append(animal)
