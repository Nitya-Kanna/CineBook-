from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.booking import Booking
    from app.models.movie import Movie
    from app.models.screen import Screen
    from app.models.seat import Seat


class Showtime(Base):
    __tablename__ = "showtimes"
    __table_args__ = (
        CheckConstraint("price_cents >= 0", name="ck_showtimes_price_non_negative"),
        UniqueConstraint("screen_id", "starts_at", name="uq_showtimes_screen_starts_at"),
        Index("ix_showtimes_movie_starts", "movie_id", "starts_at"),
        Index("ix_showtimes_starts_at", "starts_at"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movies.id", ondelete="RESTRICT"),
        nullable=False,
    )
    screen_id: Mapped[int] = mapped_column(
        ForeignKey("screens.id", ondelete="RESTRICT"),
        nullable=False,
    )
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    price_cents: Mapped[int] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    movie: Mapped["Movie"] = relationship(back_populates="showtimes")
    screen: Mapped["Screen"] = relationship(back_populates="showtimes")
    seats: Mapped[list["Seat"]] = relationship(
        back_populates="showtime",
        cascade="all, delete-orphan",
    )
    bookings: Mapped[list["Booking"]] = relationship(back_populates="showtime")
