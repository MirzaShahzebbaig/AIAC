import io
import unittest
from unittest.mock import patch
from task0 import simple_calculator
class TestSimpleCalculator(unittest.TestCase):
	def run_with_inputs(self, inputs):
		fake_stdin = io.StringIO("\n".join(inputs))
		with patch('sys.stdin', fake_stdin), patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
			simple_calculator()
			return fake_stdout.getvalue()
	def test_addition(self):
		output = self.run_with_inputs(["2", "+", "3"]) 
		self.assertIn("Simple Calculator", output)
		self.assertIn("Result: 5.0", output)
	def test_subtraction(self):
		output = self.run_with_inputs(["10", "-", "15"]) 
		self.assertIn("Result: -5.0", output)
	def test_multiplication(self):
		output = self.run_with_inputs(["1.5", "*", "4"]) 
		self.assertIn("Result: 6.0", output)
	def test_division(self):
		output = self.run_with_inputs(["9", "/", "4"]) 
		self.assertIn("Result: 2.25", output)
	def test_division_by_zero(self):
		output = self.run_with_inputs(["7", "/", "0"]) 
		self.assertIn("Error: Division by zero.", output)
		self.assertNotIn("Result:", output.splitlines()[-1])
	def test_invalid_operator(self):
		output = self.run_with_inputs(["5", "^", "2"]) 
		self.assertIn("Invalid operator.", output)
	def test_invalid_number_input(self):
		output = self.run_with_inputs(["abc"]) 
		self.assertIn("Invalid input. Please enter numeric values.", output)
if __name__ == '__main__':
	unittest.main()
