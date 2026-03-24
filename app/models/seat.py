from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Index, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.booking import Booking
    from app.models.showtime import Showtime


class Seat(Base):
    __tablename__ = "seats"
    __table_args__ = (
        CheckConstraint("seat_number >= 1", name="ck_seats_seat_number_positive"),
        UniqueConstraint(
            "showtime_id",
            "row_label",
            "seat_number",
            name="uq_seats_showtime_row_seat",
        ),
        Index("ix_seats_showtime_id", "showtime_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    showtime_id: Mapped[int] = mapped_column(
        ForeignKey("showtimes.id", ondelete="CASCADE"),
        nullable=False,
    )
    row_label: Mapped[str] = mapped_column(String, nullable=False)
    seat_number: Mapped[int] = mapped_column(nullable=False)

    showtime: Mapped["Showtime"] = relationship(back_populates="seats")
    bookings: Mapped[list["Booking"]] = relationship(back_populates="seat")
