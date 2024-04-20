# start

class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MAX_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
            return
        self.__status = True
        return

    def mute(self):
        if self.__muted:
            self.__muted = False
            return
        self.__muted = True
        return

    def channel_up(self):
        if self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
            return
        self.__channel = Television.MIN_CHANNEL
        return

    def channel_down(self):
        if self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
            return
        self.__channel = Television.MAX_CHANNEL
        return

    def volume_up(self):
        if self.__channel < Television.MAX_VOLUME:
            self.__channel += 1
            return
        self.__channel = Television.MIN_VOLUME
        return

    def volume_down(self):
        if self.__channel < Television.MIN_VOLUME:
            self.__channel -= 1
            return
        self.__channel = Television.MAX_VOLUME
        return

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'





