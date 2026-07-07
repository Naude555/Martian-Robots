from dataclasses import dataclass

@dataclass
class World:
    max_x: int
    max_y: int
    scents: set[tuple[int, int, str]]