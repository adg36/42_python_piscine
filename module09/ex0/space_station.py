#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    valid_data = {
        'station_id': 'LGW125',
        'name': 'Titan Mining Outpost',
        'crew_size': 6,
        'power_level': "76.4",
        'oxygen_level': 95.5,
        'last_maintenance': '2023-07-11T00:00:00',
        'is_operational': True,
        'notes': None
    }

    print("Space Station Data Validation\n"
          "========================================")

    try:
        station = SpaceStation(**valid_data)
        print("Valid station created:")
        print(
            f"ID: {station.station_id}\n"
            f"Name: {station.name}\n"
            f"Crew: {station.crew_size} people\n"
            f"Power: {station.power_level}%\n"
            f"Oxygen: {station.oxygen_level}%\n"
            f"Status: {'Operational' if station.is_operational else 'Idle'}"
        )

        if station.notes is not None:
            print(f"Notes: {station.notes}")

    except ValidationError as e:
        for err in e.errors():
            print(f"{err['loc'][0]}: {err['msg']}")

    invalid_data = {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 26,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2026-02-25T00:00:00'
    }

    try:
        SpaceStation(**invalid_data)
    except ValidationError as e:
        print("\n========================================")
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
