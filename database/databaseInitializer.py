from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.model.baseModel import Base

#Important
from database.model.productModel import ProductModel
from database.model.reviewModel import ReviewModel

DATABASE_URL = "sqlite:///myBdd.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def get_connection():
    db = Session()
    try:
        yield db
    finally:
        db.close()
