from pydantic import BaseModel


class Carrier(BaseModel):
    name: str
    trucksPerDay: int


class CarriersResponse(BaseModel):
    from_city: str
    to_city: str
    carriers: list[Carrier]
