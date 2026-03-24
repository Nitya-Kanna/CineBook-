from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.showtime import Showtime


class Screen(Base):
    __tablename__ = "screens"
    __table_args__ = (
        CheckConstraint("rows_count > 0", name="ck_screens_rows_positive"),
        CheckConstraint("seats_per_row > 0", name="ck_screens_seats_per_row_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    rows_count: Mapped[int] = mapped_column(nullable=False)
    seats_per_row: Mapped[int] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    showtimes: Mapped[list["Showtime"]] = relationship(back_populates="screen")
