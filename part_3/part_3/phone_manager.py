# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        for old_emp in self.employees:
            if employee.id == old_emp.id: raise PhoneError()

        self.employees.append(employee)


    def add_phone(self, phone):
        for emp_phone in self.phones:
            if phone.id == emp_phone.id: raise PhoneError()

        self.phones.append(phone)


    def assign(self, phone_id, employee):
        # Find phone in phones list

        phone_in_list = False
        for phone in self.phones:
            phone_ids_match = phone.id == phone_id
            phone_emp_ids_match = phone.employee_id == employee.id

            if phone_ids_match and phone.employee_id and not phone_emp_ids_match:
                raise PhoneError()
            elif phone_emp_ids_match and not phone_ids_match:
                raise PhoneError()
            elif phone_ids_match:
                phone_in_list = True

        if phone_in_list: phone.assign(employee.id)


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list

        if employee not in self.employees:
            raise PhoneError()

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None


class PhoneError(Exception):
    pass
