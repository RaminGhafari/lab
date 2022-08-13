import pytest
from classes import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_init(self):
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv2.power()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'

    def test_channel_down(self):
        self.tv2.power()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv2.channel_down()
        self.tv2.channel_down()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv2.power()
        self.tv2.channel_down()
        self.tv2.channel_down()
        assert self.tv2.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'

    def test_volume_up(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv2.power()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv2.volume_up()
        self.tv2.volume_up()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv2.volume_down()
        self.tv2.volume_down()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv2.volume_down()
        assert self.tv2.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv2.power()
        self.tv2.volume_down()
        assert self.tv2.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
