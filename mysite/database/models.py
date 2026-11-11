from .db import Base
from sqlalchemy import String, Integer, Date, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, datetime, timezone
from typing import Optional, List
from enum import Enum as PyEnum


class ApplicationStatusChoices(str, PyEnum):
    applied = 'applied'
    accepted = 'accepted'
    rejected = 'rejected'
    pending = 'pending'


class UserProfile(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[Optional[str]] = mapped_column(String, unique=True, nullable=True)
    job: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String)
    registered_date: Mapped[date] = mapped_column(Date, default=date.today)

    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user', cascade='all, delete-orphan')


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')


