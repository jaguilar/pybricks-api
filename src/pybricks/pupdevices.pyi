# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2022 The Pybricks Authors

from typing import Collection, List, Optional, Tuple, Union

from ._common import (
    Keypad,
    DCMotor as _DCMotor,
    ColorLight,
    LightArray,
    Motor as _Motor,
    Light as BaseLight,
)

from .parameters import Color, Direction, Port

class DCMotor(_DCMotor): ...

class Motor(_Motor):
    def reset_angle(self, angle: Optional[int]) -> None: ...

class Remote:
    light: ColorLight
    buttons: Keypad
    addresss: Union[str, None]
    def __init__(self, address: str = None, timeout: int = 10000): ...

class TiltSensor:
    def __init__(self, port: Port): ...
    def tilt(self) -> Tuple[int, int]: ...

class ColorDistanceSensor:
    light: ColorLight
    def __init__(self, port: Port): ...
    def color(self) -> Optional[Color]: ...
    def ambient(self) -> int: ...
    def reflection(self) -> int: ...
    def detectable_colors(self, colors: Collection[Color]) -> None: ...
    def hsv(self) -> Color: ...
    def distance(self) -> int: ...

class PFMotor(DCMotor):
    def __init__(
        self,
        sensor: ColorDistanceSensor,
        channel: int,
        color: Color,
        positive_direction: Direction = Direction.CLOCKWISE,
    ): ...

class ColorSensor:
    lights: LightArray
    def __init__(self, port: Port): ...
    def color(self, surface: bool = True) -> Optional[Color]: ...
    def detectable_colors(self, colors: Collection[Color]) -> None: ...
    def hsv(self, surface: bool = True) -> Color: ...
    def ambient(self) -> int: ...
    def reflection(self) -> int: ...

class UltrasonicSensor:
    lights: LightArray
    def __init__(self, port: Port): ...
    def distance(self) -> int: ...
    def presence(self) -> bool: ...

class ForceSensor:
    def __init__(self, port: Port): ...
    def force(self) -> int: ...
    def distance(self) -> int: ...
    def pressed(self, force: int = 3) -> bool: ...
    def touched(self) -> bool: ...

class ColorLightMatrix:
    def __init__(self, port: Port) -> None: ...
    def on(self, color: Union[Color, List[Color]]) -> None: ...
    def off(self) -> None: ...

class InfraredSensor:
    def __init__(self, port: Port): ...
    def reflection(self) -> int: ...
    def distance(self) -> int: ...
    def count(self) -> int: ...

class Light(BaseLight):
    def __init__(self, port: Port): ...