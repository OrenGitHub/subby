from attrs import define

@define
class Address:

    street: str
    city: str

    def is_big_city(self) -> bool:
        return self.city == "NYC"
