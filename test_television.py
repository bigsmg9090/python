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

	def test_power(self):
		self.t1.power()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 0"
		assert str(self.t2) == "Power = False, Channel = 0, Volume = 0"

	def test_mute(self):
		self.t1.power()
		self.t1.volume_up()
		self.t1.mute()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 0"
		self.t2.volume_up()
		self.t2.volume_up()
		self.t2.mute()
		assert str(self.t2) == "Power = False, Channel = 0, Volume = 0"

	def test_channel_change(self):
		self.t1.power()
		self.t1.channel_up()
		assert str(self.t1) == "Power = True, Channel = 1, Volume = 0"
		self.t2.power()
		self.t2.channel_down()
		self.t2.channel_down()
		assert str(self.t2) == "Power = True, Channel = 2, Volume = 0"
		self.t1.power()
		self.t1.channel_up()
		assert str(self.t1) == "Power = False, Channel = 1, Volume = 0"

	def test_volume_change(self):
		self.t1.power()
		self.t1.volume_up()
		self.t1.volume_up()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 2"
		# mute effects
		self.t1.mute()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 0"
		self.t1.volume_down()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 1"
		self.t1.mute()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 0"
		self.t1.volume_up()
		assert str(self.t1) == "Power = True, Channel = 0, Volume = 2"
		# power off
		self.t2.volume_up()
		assert str(self.t2) == "Power = False, Channel = 0, Volume = 0"
