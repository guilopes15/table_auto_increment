from pydantic import BaseModel


class Product(BaseModel):
    name: str
    quantity: int
    description: str


class Message(BaseModel):
    message: str
