from person import Person


class Administration(Person):
    def __init__(self, name, employee_id, job_title):
        super().__init__(name, employee_id)
        self.job_title = job_title


class Zookeeper(Person):
    def __init__(self, name, employee_id, assigned_enclosures: list):
        super().__init__(name, employee_id)
        self.assigned_enclosures = assigned_enclosures
