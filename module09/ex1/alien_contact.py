#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing_extensions import Self


class ContactType(str, Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_values(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Field contact_id must start with "AC"')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if (
                self.contact_type == ContactType.TELEPATHIC
                and self.witness_count < 3):
            raise ValueError(
                'Telepathic contact requires at least 3 witnesses')
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages')
        return self


def main() -> None:
    valid_data = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-04-13T00:00:00',
        'contact_type': 'radio',
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli'
    }

    print("Alien Contact Log Validation\n"
          "======================================")
    try:
        report = AlienContact(**valid_data)
        print("Valid contact report:")
        print(
            f"ID: {report.contact_id}\n"
            f"Type: {report.contact_type.value}\n"
            f"Location: {report.location}\n"
            f"Signal: {report.signal_strength}/10\n"
            f"Duration: {report.duration_minutes} minutes\n"
            f"Witnesses: {report.witness_count}")

        if (
                report.message_received is not None
                and report.message_received != ""):
            print(f"Message: '{report.message_received}'")

    except ValidationError as e:
        for err in e.errors():
            print(f"{err['msg']}")

    invalid_data = {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-04-20T00:00:00',
        'contact_type': 'telepathic',
        'location': 'Area 51, Nevada',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 2,
        'message_received': 'Greetings from Zeta Reticuli'
    }

    try:
        AlienContact(**invalid_data)
    except ValidationError as e:
        print("\n=====================================")
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
