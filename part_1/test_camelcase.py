from unittest import TestCase
import camelcase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelcase.camelCaseify('Hello World'))
        self.assertEqual('', '')
        self.assertEqual('hello!orld', camelcase.camelCaseify('Hello !orld'))

