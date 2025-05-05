from enum import Enum as PyEnum

from sqlalchemy import BIGINT
from sqlalchemy import Enum as SQLAEnum
from sqlalchemy import ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

from db import Base
from db.utils import CreatedModel



class User(CreatedModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)


class Category(CreatedModel):
    __tablename__ = "categories"
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    name: Mapped[str]


# class Product(CreatedModel):
#     class StatusType(PyEnum):
#         PENDING = "pending"
#         REJECT = "reject"
#         ACCEPT = "accept"
#     __tablename__ = "products"
#     id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
#     name: Mapped[str]
#     description: Mapped[str]
#     users_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('usersid', ondelete="CASCADE"))
#     price: Mapped[float] = mapped_column(DECIMAL(10, 0))
#     categories_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('categories.chat_id', ondelete="CASCADE"))
#     deadline: Mapped[str]
#     status: Mapped[str] = mapped_column(SQLAEnum(StatusType, values_callable=lambda x: [i.value for i in x]),
#                                         server_default=StatusType.PENDING.value)


metadata = Base.metadata
