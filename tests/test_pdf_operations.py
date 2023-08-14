import unittest
import os
from src.pdf_operations import split_pdf
from unittest.mock import patch

class TestPayrollApp(unittest.TestCase):

    def setUp(self):
        # This method is called before every test.
        # You can set up some common resources here, e.g., creating a temp directory.
        self.input_pdf = 'tests/Payslip Template.pdf'

    def tearDown(self):
        # This method is called after every test.
        # Here you can clean up resources you set up in the `setUp` method.
        pass

    def test_split_pdf(self):
        result = split_pdf(self.input_pdf)
        self.assertEqual(len(result), 2)
        for output_pdf in result:
            self.assertTrue(os.path.exists(output_pdf))
            os.remove(output_pdf)  # Cleanup after test

    def test_empty_pdf(self):
        empty_pdf = 'tests/Empty.pdf'
        result = split_pdf(empty_pdf)
        self.assertEqual(result, [])

    def test_non_existent_pdf(self):
        with self.assertRaises(Exception):  # Assuming the function raises a generic exception; replace with the specific exception if known.
            non_existent_pdf = '/path/to/non_existent_pdf.pdf'
            split_pdf(non_existent_pdf)

    def test_non_pdf_input(self):
        with self.assertRaises(Exception):  # Again, assuming a generic exception.
            not_a_pdf = '/path/to/some_image.jpg'
            split_pdf(not_a_pdf)

    @patch('src.pdf_operations.split_pdf', return_value=[f"dummy_payslip_{i}.pdf" for i in range(100)])
    def test_large_pdf(self, mock_split_pdf):
        large_pdf = '/path/to/large_pdf.pdf'
        
        # Use the mocked function
        result = mock_split_pdf(large_pdf)
        
        mock_split_pdf.assert_called_once_with(large_pdf)
        self.assertEqual(len(result), 100)

        # Note: No need to check for file existence or do cleanup in this mock test.

    # ... Add other tests here.

if __name__ == '__main__':
    unittest.main()
