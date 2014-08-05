import os
import pytest


def run_tests():
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	pytest.main('all_tests.py')
