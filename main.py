from fastapi import FastAPI, Depends
from typing import List
from sqlmodel import SQLModel, Session, select

from config import setup_cors
from db import engine, get_session
from models.product import Product
from models.category import Category
from models.order import Order



class OrderRead(SQLModel):
    date: str
    price: float
    status: str

class OrderCreate(SQLModel):
    date: str
    price: float
    status: str

class ProductRead(SQLModel):
    name: str
    imgPath: str
    price: float

class ProductCreate(SQLModel):
    name: str
    imgPath: str
    price: float
    category_id: int
    is_popular: bool = False


class CategoryRead(SQLModel):
    name: str
    products: List[ProductRead] = []

class CategoryCreate(SQLModel):
    name: str




app = FastAPI()
setup_cors(app)

SQLModel.metadata.create_all(engine)


@app.get("/")
def root():
    return {"Hello": "World!", "Server Status": "Active"}




@app.get("/products/", response_model=List[ProductRead], tags=["Products"])
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()

@app.post("/products/", response_model=ProductRead, tags=["Products"])
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product



@app.get("/frequent-products", response_model=List[ProductRead], tags=["Products"])
def list_frequent_products(session: Session = Depends(get_session)):
    return session.exec(select(Product).where(Product.is_popular == 1)).all()



@app.get("/categories", response_model=List[CategoryRead], tags=["Categories"])
def list_categories(session: Session = Depends(get_session)):
    return session.exec(select(Category)).all()

@app.post("/categories/", response_model=CategoryRead, tags=["Categories"])
def create_category(category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = Category.from_orm(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category




@app.get("/orders/", response_model=List[OrderRead], tags=["Orders"])
def list_orders(session: Session = Depends(get_session)):
    return session.exec(select(Order)).all()

@app.post("/orders/", response_model=OrderRead, tags=["Orders"])
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    db_order = Order.from_orm(order)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order