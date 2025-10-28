from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.model.baseModel import BaseModel

class ReviewModel(BaseModel):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String)
    rating: Mapped[int] = mapped_column(Integer)

    product_id = mapped_column(Integer, ForeignKey("product.id"), nullable=False)

    product = relationship("ProductModel", back_populates="reviews")
