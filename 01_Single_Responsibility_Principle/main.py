from employee import Employee
from storage import EmployeeStorage

e = Employee("John", 2000)
s = EmployeeStorage()
s.save_as_json(e)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     pass
