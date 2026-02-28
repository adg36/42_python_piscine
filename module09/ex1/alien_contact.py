#!/usr/bin/env python3


from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from typing_extensions import Self


def main() -> None:

    class ContactType(str, Enum):
        radio = 'radio'
        visual = 'visual'
        physical = 'physical'
        telepathic = 'telepathic'


    class Model(BaseModel):
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
        if self.contact_type is 'physical' and not is_verified:
            raise ValueError('Physical contact reports must be verified')
        if self.contact_type is 'telepathic' and witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')
        if signal_strength > 7.0 and message_received is None:
            raise ValueError('Strong signals (> 7.0) should include received messages')
        return self
   
    data = {
            'contact_id': 'AC_2024_001',
            'timestamp': '13-04-2024T00:00:00',
            'contact_type': 'radio',
            'location': 'Area 51, Nevada',
            'signal_strength': 8.5,
            'duration_minutes': 45,
            'witness_count': 5,
            'message_received': 'Greetings from Zeta Reticuli'
    }

    mymodel = Model(**data)

    print("Alien Contact Log Validation\n"
          "======================================")
    print("Valid contact report:\n"
          f"ID: {mymodel.contact_id}\n"
          f"Type: {mymodel.contact_type}\n"
          f"Location: {mymodel_location}\n"
          f"Signal: {mymodel_signal_strength}\n"
          f"Duration: {mymodel.duration_minutes}\n"
          f"Witnesses: {mymodel.witness_count}\n")
    if data['message_received'] is not None:
        print(f"Message: '{mymodel.message_received}'\n")

    print("=====================================\n"
          "Expected validation error:")
    try:
        mymodel_error = Model(**data)
        print(f"Type: {mymodel_error.contact_type}\n")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
