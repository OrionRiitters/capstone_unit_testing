'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_then_remove_student(self):
        test_class = ClassList(1)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    def test_remove_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Ooh')
        test_class.add_student('Ah')
        self.assertEquals(2, len(test_class.class_list))

        with self.assertRaises(StudentError):
            test_class.remove_student('Croomple')



    def test_remove_student_from_empty_list(self):
        test_class = ClassList(0)

        with self.assertRaises(StudentError):
            test_class.remove_student('Fake Student')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    def test_is_enrolled_on_student_not_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Poiu')
        test_class.add_student('Whomp')
        self.assertEquals(2, len(test_class.class_list))

        self.assertFalse(test_class.is_enrolled('Cardboard Box'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    def test_is_class_full(self):
        test_class = ClassList(4)
        test_class.add_student('asdf')
        test_class.add_student('af')
        test_class.add_student('ffff')
        test_class.add_student('asdfdsa')

        self.assertTrue(test_class.class_is_full())


    def test_class_not_full(self):
        test_class_not_full = ClassList(5)
        test_class_empty = ClassList(5)

        test_class_not_full.add_student('asdf')
        test_class_not_full.add_student('af')
        test_class_not_full.add_student('ffff')
        test_class_not_full.add_student('asdfdsa')

        self.assertFalse(test_class_not_full.class_is_full())
        self.assertFalse(test_class_empty.class_is_full())


    def test_index_of_student_on_empty_list(self):
        test_class = ClassList(0)

        self.assertEquals(None, test_class.index_of_student('No'))


    def test_index_of_student_not_in_list(self):
        test_class = ClassList(1)
        test_class.add_student('A student!')

        self.assertEquals(None, test_class.index_of_student('No'))

