from __future__ import annotations

from datetime import UTC, datetime, timedelta, timezone

from sqlalchemy import DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from database import Base
import secrets

class UserSession(Base):
    __tablename__="user_sessions"
    session_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    expire_time: Mapped[datetime]= mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)+timedelta(days=1))
    questions: Mapped[list["Question"]]=relationship(back_populates="session",cascade="all, delete-orphan")



class Question(Base):
    __tablename__ = "questions"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    session_id: Mapped[str] = mapped_column(String(64), ForeignKey('user_sessions.session_id'))
    date_posted: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )
    response_text: Mapped[str] = mapped_column(Text, nullable=False)
    session: Mapped["UserSession"] = relationship(back_populates="questions")