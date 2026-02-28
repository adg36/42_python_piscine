#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import Optional
from typing_extensions import Self
from pydantic import BaseModel, conlist, Field, ValidationError


class Rank(str, Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: conlist(CrewMember, min_items=1, max_items=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        if not Rank.CAPTAIN in self.crew or Rank.COMMANDER in self.crew:
            raise ValueError('Must have at least one Commander or Captain')
        if self.duration_days > 365 and
        return self

# helper to check if 50% of crew has more than 5 years of experience

# helper to check if all crew members are active

def main() -> None:


if __name__ == "__main__":
    main()
