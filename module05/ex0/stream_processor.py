#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data: "
                             "expected list/tuple of numbers")

        try:
            count = len(data)
            total = sum(data)
            average = total / count if count > 0 else 0.0

            result = (f"Processed {count} numeric values, "
                      f"sum={total}, avg={average}")
            return result
        except Exception as e:
            raise ValueError(f"Error processing numeric data: {str(e)}")

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, (list, tuple)):
                return False
            for num in data:
                if not isinstance(num, (int, float)) or isinstance(num, bool):
                    return False
            return len(data) > 0
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data: expected non-empty string")

        try:
            char_count = len(data)
            word_count = len(data.split())

            result = (f"Processed text: {char_count} "
                      f"characters, {word_count} words")
            return result
        except Exception as e:
            raise ValueError(f"Error processing text data: {str(e)}")

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str) and len(data) > 0
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data: "
                             "expected string with log level")
        try:
            self.level = data.split(": ")[0]
            self.message = data.split(": ")[1]

            if self.level == "ERROR":
                level = "[ALERT]"
            else:
                level = "[INFO]"
            result = f"{level} {self.level} level detected: {self.message}"
            return result
        except Exception as e:
            raise ValueError(f"Error processing log data: {str(e)}")

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str) or len(data) == 0:
                return False
            if (data.startswith("ERROR:") or data.startswith("INFO:")):
                return True
            return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def demonstrate_polymorphism(processors: List[DataProcessor],
                             test_data: List[Any]) -> None:
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    for i, (processor, data) in enumerate(zip(processors, test_data), 1):
        try:
            result = processor.process(data)
            print(f"Result {i}: {result}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")


def ft_stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    
    processors = {
            "Numeric": (NumericProcessor(), [1, 2, 3, 4, 5]),
            "Text": (TextProcessor(), "Hello Nexus World"),
            "Log": (LogProcessor(), "ERROR: Connection timeout")
    }
    for name, (processor, data) in processors.items():
        print(f"\nInitializing {name} Processor...")
        if type(data) is str:
            print(f'Processing data: "{data}"')
        else:
            print(f'Processing data: {data}')
        result = processor.process(data)
        if processor.validate(data):
            print(f"Validation: {name} data verified")
        else:
            print(f"Validation error: Could not verify {name.lower()} data.")
        print(processor.format_output(result))

    # polymorphism demonstration
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data = [[1, 2, 3], "Yellow Banana", "INFO: System ready"]
    demonstrate_polymorphism(processors, test_data)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    ft_stream_processor()
