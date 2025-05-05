from enum import Enum as PyEnum

from sqlalchemy import BIGINT
from sqlalchemy import Enum as SQLAEnum
from sqlalchemy import ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

from db import Base
from db.utils import CreatedModel


# engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/tg_bot_p30")
# session = sessionmaker(engine)()
# Base = declarative_base()

class User(CreatedModel):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)


class Developer(CreatedModel):
    __tablename__ = "developers"
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    username: Mapped[str]
    occupation: Mapped[str]
    description: Mapped[str]


class Category(CreatedModel):
    __tablename__ = "categories"
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    name: Mapped[str]


class Project(CreatedModel):
    class StatusType(PyEnum):
        REJECT = "reject"
        ACCEPT = "accept"
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    developer_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('developers.chat_id', ondelete="CASCADE"))
    price: Mapped[float] = mapped_column(DECIMAL(10, 0))
    customer_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('customers.chat_id', ondelete="CASCADE"))
    deadline: Mapped[str]
    tz_file: Mapped[str]
    status: Mapped[str] = mapped_column(SQLAEnum(StatusType, values_callable=lambda x: [i.value for i in x]),
                                        server_default=StatusType.ACCEPT.value)


metadata = Base.metadata
