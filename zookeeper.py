from person import Person


class Administration(Person):
    def __init__(self):
        name = input('Enter the name: ')
        employee_id = input('Введіть префікс для id: ')
        super().__init__(name, employee_id)
        self.__job_title = input('Enter the job title: ')
        Person.add_person_to_list(self)
        # print('list: ', self.list_persons)


    # def add_person(self):
    #     Person.list_persons = self
    def __str__(self):
        return f'{self.__job_title}\t-\tid: {self.employee_id}, name: {self.name}'


class Zookeeper(Person):
    def __init__(self, name, employee_id, assigned_enclosures: list):
        super().__init__(name, employee_id)
        self.__assigned_enclosures = assigned_enclosures # list of enclosures

    def __str__(self):
        return f'Zookeeper\t-\tid: {self.employee_id}, {self.name}, '

    @property
    def assigned_enclosures(self):
        return (assigned_enclosures for assigned_enclosures in self.__assigned_enclosures)

    @assigned_enclosures.setter
    def assigned_enclosures(self, enclosure):
        self.__assigned_enclosures.append(enclosure)
