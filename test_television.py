from television import *
import pytest

class Test:
	def setup_method(self):
		self.t1 = Television()
		self.t2 = Television()

	def teardown_method(self):
		del self.t1
		del self.t2

	def test_init(self):
		assert str(self.t1) == "Power = False, Channel = 0, Volume = 0"

	# def test_set_make(self):
	# 	self.cl.set_make('BMW')
	# 	assert self.c1.get_make == 'BMW' assert self.c2.get_make() == 'Honda'
	# def test_str(self):
	# 	assert self.cl.__str__( == 'Year = 2000'
	# 	assert self.c2.__str__( == 'Year = 2000'