from dataclasses import dataclass, field

Scent = tuple[int, int, str]


@dataclass
class World:
    max_x: int
    max_y: int
    scents: set[Scent] = field(default_factory=set)

    def contains(self, x: int, y: int) -> bool:
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def has_scent(self, x: int, y: int, direction: str) -> bool:
        return (x, y, direction) in self.scents

    def add_scent(self, x: int, y: int, direction: str) -> None:
        self.scents.add((x, y, direction))
