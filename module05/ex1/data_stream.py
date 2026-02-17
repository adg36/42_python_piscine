#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0
        self.error_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        try:
            filtered = [item for item in data_batch
                        if criteria.lower() in str(item).lower()]
            return filtered
        except Exception as e:
            print(f"Filter error in {self.stream_id}: {e}")
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count,
            "error_count": self.error_count
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        self.processed_count = 0
        self.total_readings = 0
        self.sum_temp = 0
        self.name = "Sensor"
        self.ops = "readings"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_readings += len(data_batch)
            self.sum_temp += sum(data_batch)
            self.processed_count += 1

            avg_temp = self.sum_temp / self.total_readings

            return (f"Sensor analysis: {self.total_readings} readings "
                    f"processed, avg temp: {avg_temp:.1f}°C")
        except Exception as e:
            self.error_count += 1
            return f"Sensor processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            try:
                critical = [temp for temp in data_batch if temp > 30]
                return critical
            except Exception:
                return super().filter_data(data_batch, criteria)
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["total_readings"] = self.total_readings
        stats["avg_temp"] = (
                self.sum_temp / self.total_readings
                if self.total_readings > 0
                else 0.0
        )
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.processed_count = 0
        self.net_flow = 0
        self.name = "Transaction"
        self.ops = "operations"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for item in data_batch:
                self.net_flow += item
                self.processed_count += 1

            sign = '+' if self.net_flow >= 0 else ''
            return (f"Transaction analysis: "
                    f"{self.processed_count} operations, "
                    f"net flow: {sign}{self.net_flow} units")
        except Exception as e:
            self.error_count += 1
            return f"Transaction processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            try:
                large_trans = [
                        item for item in data_batch
                        if item > 100
                ]
                return large_trans
            except Exception:
                return super().filter_data(data_batch, criteria)
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["total_transactions"] = self.processed_count
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.processed_count = 0
        self.total_events = 0
        self.error_events = 0
        self.name = "Event"
        self.ops = "events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = len(data_batch)
            errors = sum(
                    1 for item in data_batch
                    if 'error' in str(item).lower()
            )

            self.total_events += events
            self.error_events += errors
            self.processed_count += 1

            error_text = (f", {errors} error detected" if errors == 1 else
                          f", {errors} errors detected" if errors > 1 else "")
            return f"Event analysis: {events} events{error_text}"
        except Exception as e:
            self.error_count += 1
            return f"Event processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "errors":
            return [
                    item for item in data_batch
                    if 'error' in str(item).lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["total_events"] = self.total_events
        stats["error_events"] = self.error_events
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)
        else:
            raise TypeError("Only DataStream instances can be added")

    def process_all(self, batches: Dict[str, List[Any]]) -> List[str]:
        results: List[str] = []

        for stream in self.streams:
            try:
                stream_id = stream.stream_id
                if stream_id in batches:
                    result = stream.process_batch(batches[stream_id])
                    results.append(f"- {stream.name} data: "
                                   f"{stream.processed_count} {stream.ops} processed")
            except Exception as e:
                results.append(f"- Error processing {stream.stream_id}: {e}")

        return results

    def filter_all(self, batches: Dict[str, List[Any]],
                   criteria: Dict[str, str]) -> Dict[str, List[Any]]:
        filtered_results: Dict[str, List[Any]] = {}

        for stream in self.streams:
            try:
                stream_id = stream.stream_id
                if stream_id in batches and stream_id in criteria:
                    filtered = stream.filter_data(batches[stream_id],
                                                  criteria[stream_id])
                    filtered_results[stream_id] = filtered
            except Exception as e:
                print(f"Filter error for {stream.stream_id}: {e}")
        return filtered_results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    
    stream_proc = StreamProcessor()

    data = [
            (SensorStream("SENSOR_001"),[25.0, 27.5, 22.5, 35.7]),
            (TransactionStream("TRANS_001"), [100, -150, 75]),
            (EventStream("EVENT_001"), ["login", "error", "logout"])
    ]
    for stream, batch in data:
        print(f"\nInitializing {stream.name} Stream...")
        print(f"Stream ID: {stream.stream_id},"
              f" Type: {stream.stream_type}")
        result = stream.process_batch(batch)
        print(f"Processing {stream.name.lower()} batch: {batch}\n"
              f"{result}")
        stream_proc.add_stream(stream)

    print("\n=== Polymorphic Sream Processing ===\n"
          "Processing mixed stream types through unified interface...\n")
    batches = {
            "SENSOR_001": [25.0, 27.5, 22.5, 35.7],
            "TRANS_001": [100, -150, 75],
            "EVENT_001": ["login", "error", "logout"]
    }
    print("Batch 1 Results:")
    results = stream_proc.process_all(batches)
    for result in results:
        print(result)
    

if __name__ == "__main__":
    data_stream()
