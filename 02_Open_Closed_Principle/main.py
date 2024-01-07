# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#
# class Manager(Employee):
#     def __init__(self, name, department):
#         super().__init__(name)
#         self.department = department
#
#
# def print_employee(e):
#     if type(e) is Employee:
#         print(f'{e.name} is an employee')
#     elif type(e) is Manager:
#         print(f'{e.name} leads department {e.department}')

"""
It now becomes very clear that we cannot extend the
functionality without changing the existing working code.
And there is the risk of changing the code in one place
but forget it in another place. This example is a
violation of the open-closed principle.
"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f'{self.name} is an employee'


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def get_info(self):
        return f'{self.name} leads department {self.department}'


def print_employee(person):
    print(person.get_info())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    emp = Employee('John')
    m = Manager('Khosro', department='Energy')
    print_employee(emp)
    print_employee(m)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
