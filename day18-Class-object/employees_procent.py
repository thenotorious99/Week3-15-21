class Employee:
    def __init__(self, name, position, payment):
        self.name = name
        self.position = position
        self.payment = payment

    def procent_more(self):
        if self.position == "Director":
            percent = 0.20
        elif self.position == "Manager":
            percent = 0.10
        else:
            percent = 0.5
        self.payment += self.payment * percent
        return self.payment

company_employee = Employee("John", "Director", 1500)

print(company_employee.procent_more())
