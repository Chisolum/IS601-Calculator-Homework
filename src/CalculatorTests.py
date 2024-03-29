import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
from decimal import Decimal
import math

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
         self.calculator = Calculator()

    def tearDown(self):
        if CsvReader.data is not None:
            CsvReader.data = []

    def test_instantiate_Calculator(self):
           self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
                self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
                test_data = CsvReader('/src/Addition.csv').data
                for row in test_data:
                    self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
                    self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('/src/Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('/src/Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('/src/Square Root.csv').data
        for row in test_data:
            pprint(row)
            self.assertEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))



if __name__ == '__main__':
    unittest.main()
