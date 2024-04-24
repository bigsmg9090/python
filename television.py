# start

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initializes a Television object. Default:
            power status is off
            muted status is off
            volume is at min volume (0 of 2)
            channel is at min channel (0 of 3)"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = self.__volume

    def power(self) -> None:
        """Changes the power status of the TV"""
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """Changes the mute status of the TV"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """Increases the TV channel by 1 if the power is on"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases the TV channel by 1 if the power is on"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the TV volume by 1 if the power is on"""
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False

    def volume_down(self) -> None:
        """Decreases the TV volume by 1 if the power is on"""
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False

    def __str__(self) -> str:
        """Returns a str containing the power status, channel, and volume of the instance"""
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'







