from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import Column, String
from typing import Optional


class Product(SQLModel, table=True):
    prod_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    imgPath: str = Field(sa_column=Column("image_path", String))
    price: float
    cat_id: int = Field(foreign_key="category.cat_id")
    is_popular: int

    category: "Category" = Relationship(back_populates="products")
