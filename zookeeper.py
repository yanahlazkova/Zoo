from person import Person


class Employee(Person):
    __pref_id = 'em00-'
    __zookeeper = False

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
        return f'{self.__job_title} (id: {self.employee_id}, name: {self.name})'

    @property
    def job_title(self):
        return self.__job_title


class Zookeeper:

    def __init__(self, employee: Employee, enclosure):
        self.__zookeeper = employee
        self.__enclosure = enclosure
        self.__list_enclosures = [enclosure] if enclosure else []

    def __str__(self):
        return f'Zookeeper\t-\tid: {self.__zookeeper}, {self.__list_enclosures}'

    @property
    def zookeeper(self):
        return self.__zookeeper

    @property
    def list_enclosures(self):
        return self.__list_enclosures

    @list_enclosures.setter
    def list_enclosures(self, new_enclosure):
        self.__list_enclosures.append(new_enclosure)
