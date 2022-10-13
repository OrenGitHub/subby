from attrs import define
from subby.src.address import Address

@define
class Person:

    name: str
    age: int
    address: Address

    def birthday(self) -> None:
        self.age += 1

