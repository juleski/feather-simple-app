import enum


class OccupationStatus(str, enum.Enum):
    employed = "employed"
    student = "student"
    self_employed = "self-employed"
