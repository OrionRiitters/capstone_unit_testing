import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)



    def test_create_and_add_new_employee(self):
        
        testEmployee1 = Employee(1, 'Mark')
        testEmployee2 = Employee(2, 'Ingrid')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

    

        self.assertIn(testEmployee1, testAssignmentMgr.employees)
        self.assertIn(testEmployee2, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):

        testEmployee1 = Employee(1, 'Mark')
        testEmployee2 = Employee(1, 'Ingrid')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmployee2)


    def test_assign_phone_to_employee(self):

        testEmployee1 = Employee(1, 'Mark')
        testPhone1 = Phone(43, 'Apple', 'iPhone 2')
        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.assign(43, testEmployee1)

        self.assertTrue(testPhone1.employee_id == 1)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):

        testEmployee1 = Employee(1, 'Mark')
        testEmployee2 = Employee(2, 'Ingrid')
        testPhone1 = Phone(43, 'Apple', 'iPhone 2')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(43, testEmployee2)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(43, testEmployee1)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        testEmployee1 = Employee(1, 'Mark')
        testPhone1 = Phone(21, 'Samsung', 'Galaxy S9')
        testPhone2 = Phone(43, 'Apple', 'iPhone 2')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.assign(43, testEmployee1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(21, testEmployee1)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        testEmployee1 = Employee(1, 'Mark')
        testPhone1 = Phone(21, 'Samsung', 'Galaxy S6')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        phone_list_1 = []
        for phone in testAssignmentMgr.phones:
            phone_list_1.append(phone)

        testAssignmentMgr.assign(21, testEmployee1)
        testAssignmentMgr.assign(21, testEmployee1)

        for phone1 in testAssignmentMgr.phones:
            for phone2 in phone_list_1:
                self.assertIn(phone1, phone_list_1)
                self.assertIn(phone2, testAssignmentMgr.phones)


    def test_un_assign_phone(self):

        testEmployee1 = Employee(1, 'Mark')
        testPhone1 = Phone(21, 'Samsung', 'Galaxy S3')
        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.assign(21, testEmployee1)
        testAssignmentMgr.un_assign(21)

        self.assertEquals(None, testPhone1.employee_id)
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None


    def test_get_phone_info_for_employee(self):

        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        testEmployee1 = Employee(1, 'Mark')
        testEmployee2 = Employee(2, 'Blunk')
        testPhone1 = Phone(43, 'Samsung', 'Galaxy S9')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_phone(testPhone1)

        testAssignmentMgr.assign(43, testEmployee1)
        empPhone = testAssignmentMgr.phone_info(testEmployee1)

        self.assertEquals(empPhone, testPhone1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.phone_info(testEmployee2)
