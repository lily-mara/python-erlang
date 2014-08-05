import os
import pytest
from erlang import extended_b_lines


class TestLineCalculation:
	def setup_class(self):
		self.cases = [(0.001, 8, 18), (0.5, 30, 21), (0.03, 2, 6)]

	def test_calcluations(self):
		for case in self.cases:
			assert extended_b_lines(case[1], case[0]) == case[2]

if __name__ == '__main__':
	filename = os.path.dirname(os.path.abspath(__file__))
	pytest.main('run_tests.py')
