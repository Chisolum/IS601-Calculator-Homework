import unittest

from CsvReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('/src/Addition.csv')
        self.csv_reader = CsvReader('/src/Subtraction.csv')
    def tearDownClass(self):
        close_test_data_file()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CsvReader)

if __name__ == '__main__':
    unittest.main()