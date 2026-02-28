#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing_extensions import Self
from pydantic import (
    BaseModel, conlist, Field, ValidationError, model_validator)


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
    crew: conlist(CrewMember, min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def has_leadership(self, crew):
        for member in crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                return True
        return False

    def experienced_crew(self, crew):
        seniors = 0
        for member in crew:
            if member.years_experience > 5:
                seniors += 1
        return True if seniors >= len(crew)/2 else False

    def all_members_active(self, crew):
        for member in crew:
            if not member.is_active:
                return False
        return True

    @model_validator(mode='after')
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        if not self.has_leadership(self.crew):
            raise ValueError('Must have at least one Commander or Captain')
        if self.duration_days > 365 and not self.experienced_crew(self.crew):
            raise ValueError('Long missions need 50% experienced crew')
        if not self.all_members_active(self.crew):
            raise ValueError('All crew members must be active')
        return self


def main() -> None:
    valid_data = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }

    print("Space Mission Crew Validation")
    print("========================================")

    try:
        mission = SpaceMission(**valid_data)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}\n"
              f"ID: {mission.mission_id}\n"
              f"Destination: {mission.destination}\n"
              f"Duration: {mission.duration_days} days\n"
              f"Budget: ${mission.budget_millions}M\n"
              f"Crew size: {len(mission.crew)}\n"
              "Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
    except ValidationError as e:
        for err in e.errors():
            print(f"{err['msg']}")

    invalid_data = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'lieutenant',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }

    try:
        SpaceMission(**invalid_data)
    except ValidationError as e:
        print("\n===================================")
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
