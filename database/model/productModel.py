from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.model.baseModel import BaseModel


class ProductModel(BaseModel):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    brand: Mapped[str] = mapped_column(String, nullable=False)

    reviews = relationship(
        "ReviewModel", back_populates="product", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<ProductModel(id={self.id}, name={self.name}, price={self.price}, brand={self.brand})>"
