from person import Person


class Administration(Person):
    def __init__(self, name, employee_id, job_title):
        super().__init__(name, employee_id)
        self.__job_title = job_title

    def __str__(self):
        return f'id: {self.employee_id}, {self.name}, '


class Zookeeper(Person):
    def __init__(self, name, employee_id, assigned_enclosures: list):
        super().__init__(name, employee_id)
        self.__assigned_enclosures = assigned_enclosures # list of enclosures

    def __str__(self):
        return f'id: {self.employee_id}, {self.name}, '

    @property
    def assigned_enclosures(self):
        return (assigned_enclosures for assigned_enclosures in self.__assigned_enclosures)

    @assigned_enclosures.setter
    def assigned_enclosures(self, enclosure):
        self.__assigned_enclosures.append(enclosure)
