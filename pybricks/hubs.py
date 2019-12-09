"""LEGO® Programmable Hubs."""
from enum import Enum
from .builtins import Speaker, Display, Battery, ColorLight, KeyPad


class EV3Brick():
    """LEGO® MINDSTORMS® EV3 Brick."""
    Port = Enum('Port', ['A', 'B', 'C', 'D', 'S1', 'S2', 'S3', 'S4'])
    speaker = Speaker()
    display = Display()
    battery = Battery()
    light = ColorLight()
    buttons = KeyPad()


class MoveHub():
    """LEGO® Powered Up Move Hub."""
    Port = Enum('Port', ['A', 'B', 'C', 'D'])
    battery = Battery()
    light = ColorLight()


class CityHub():
    """LEGO® Powered Up City Hub."""
    Port = Enum('Port', ['A', 'B'])
    battery = Battery()
    light = ColorLight()