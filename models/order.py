from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Float, String
from typing import Optional


class Order(SQLModel, table=True):
    ord_id: Optional[int] = Field(default=None, primary_key=True)
    date: str = Field(sa_column=Column("ord_date", String))
    price: float = Field(sa_column=Column("amount", Float))
    status: str
