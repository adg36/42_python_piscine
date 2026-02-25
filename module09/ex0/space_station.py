#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


def main() -> None:

    class SpaceStation(BaseModel):
        station_id: str = Field(min_length=3, max_length=10)
        name: str = Field(max_length=50)
        crew_size: int = Field(ge=1, le=20)
        power_level: float = Field(ge=0.0, le=100.0)
        oxygen_level: float = Field(ge=0.0, le=100.0)
        last_maintenance: datetime
        is_operational: bool = Field(default=True)
        notes: Optional[str] = Field(None, max_length=200)

    data = {
        'station_id': 'LGW723',
        'name': 'Mars Orbital Platform',
        'crew_size': 11,
        'power_level': 90.8,
        'oxygen_level': 87.3,
        'last_maintenance': '2023-09-25T00:00:00',
        'is_operational': False,
        'notes': 'System diagnostics required'
    }

    station = SpaceStation(**data)

    print("Space Station Data Validation\n"
          "========================================")
    print("Valid station created:\n"
          f"ID: {station.station_id}\n"
          f"Name: {station.name}\n"
          f"Crew: {station.crew_size} people\n"
          f"Power: {station.power_level}%\n"
          f"Oxygen: {station.oxygen_level}%\n"
          f"Status: {'Operational' if station.is_operational else 'Idle'}")
    if data['notes'] is not None:
        print(f"Notes: {station.notes}")

    data = {
            'station_id': 'ISS001',
            'name': 'International Space Station',
            'crew_size': 26,
            'power_level': 85.5,
            'oxygen_level': 92.3,
            'last_maintenance': '2026-02-25T00:00:00'
    }

    print("\n========================================\n"
          "Expected validation error:")
    try:
        station_error = SpaceStation(**data)
        print(f"Crew: {station_error.crew_size} people\n")
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
