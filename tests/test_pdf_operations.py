import unittest
import os
from src.pdf_operations import split_pdf

class TestPayrollApp(unittest.TestCase):

    def test_split_pdf(self):
        input_pdf = '/Users/quddusrahman/Documents/Projects/PayRollApp/tests/Payslip Template.pdf'  # Assuming a sample PDF with 2 pages in the tests directory
        result = split_pdf(input_pdf)
        self.assertEqual(len(result), 2)
        for output_pdf in result:
            self.assertTrue(os.path.exists(output_pdf))
            os.remove(output_pdf)  # Cleanup after test

if __name__ == '__main__':
    unittest.main()
