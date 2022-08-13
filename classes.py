class Television:
    """
    Class representing a TV
    """
    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a TV object
        """
        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_volume: int = Television.MIN_VOLUME
        self.__tv_status: bool = False

    def power(self) -> None:
        """
        This method checks whether TV is on or off and change its status; for example, from on to off
        and vice versa.
        """
        if self.__tv_status:
            self.__tv_status = False
        else:
            self.__tv_status = True

    def channel_up(self) -> None:
        """
        This method first checks whether the TV is on or off, then if the TV is on, this method can be
        used to change TV's channel. This method helps to go up.
        """
        if self.__tv_status:
            if self.__tv_channel == Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1

    def channel_down(self) -> None:
        """
        This method first checks whether the TV is on or off, then if the TV is on, this method can be
        used to change TV's channel. This method helps to go down.
        """
        if self.__tv_status:
            if self.__tv_channel == Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1

    def volume_up(self) -> None:
        """
        This method first checks whether the TV is on or off, then if the TV is on, this method can be
        used to change TV's volume. This method helps to turn up the TV volume.
        """
        if self.__tv_status:
            if self.__tv_volume == Television.MAX_VOLUME:
                self.__tv_volume = Television.MAX_VOLUME
            else:
                self.__tv_volume += 1

    def volume_down(self) -> None:
        """
        This method first checks whether the TV is on or off, then if the TV is on, this method can be
        used to change TV's volume. This method helps to turn down the TV volume.
        """
        if self.__tv_status:
            if self.__tv_volume == Television.MIN_VOLUME:
                self.__tv_volume = Television.MIN_VOLUME
            else:
                self.__tv_volume -= 1

    def __str__(self) -> str:
        """
        This method takes TV status, channel, and volume and returns a text (string) displaying
        the state of a TV, its channel's current value, and its volume's current value.
        :return: A text (or a string) containing TV's status, channel, and volume values.
        """
        return f'TV status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
