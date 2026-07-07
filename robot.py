from dataclasses import dataclass


@dataclass
class Robot:
    x: int
    y: int
    direction: str
    instructions: str
    lost: bool = False