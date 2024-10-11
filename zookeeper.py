from person import Person


class Employee(Person):
    __pref_id = 'em00-'

    # def __init__(self):
    def __init__(self, job_title, name):
        super().__init__(self.__pref_id, name)
        print(f'id: {self.employee_id}')
        # self.__job_title = input('Enter the job title: ')
        self.__job_title = job_title

    def to_dict(self):
        return {
            "job_title": self.__job_title,
            "name": self.__name,
        }

    def __str__(self):
        return f'{self.__job_title}\t-\tid: {self.employee_id}, name: {self.name}'

    @property
    def job_title(self):
        return self.__job_title

class Zookeeper:
    __assigned_enclosures = []

    def __init__(self, employee: Employee, enclosure):
        self.__zookeeper = employee
        self.__enclosure = enclosure
        self.__assigned_enclosures.append(self.__enclosure) # list of enclosures

    def __str__(self):
        return f'Zookeeper\t-\tid: {self.__zookeeper}, {self.__assigned_enclosures}'

    @property
    def zookeeper(self):
        return self.__zookeeper

    @property
    def assigned_enclosures(self):
        return self.__assigned_enclosures

    @assigned_enclosures.setter
    def assigned_enclosures(self, enclosure):
        self.__assigned_enclosures.append(enclosure)
