"""Constants and enums for the Contractor Finder application."""

from enum import Enum


class Specialty(str, Enum):
    """Contractor specialty types."""

    ELECTRICITY = "electricity"
    GAS = "gas"
    PLUMBING = "plumbing"
    CONSTRUCTION = "construction"
    CARPENTRY = "carpentry"
    GARDENING = "gardening"
    CLEANING = "cleaning"
    LOGISTIC = "logistic"

    def __str__(self) -> str:
        """Return the value of the enum."""
        return self.value
