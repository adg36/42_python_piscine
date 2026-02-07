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
        self.total_readings = 0
        self.sum_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [float(item.split(':')[1])
                     for item in data_batch if 'temp' in str(item)]

            self.total_readings += len(data_batch)
            self.sum_temp += sum(temps)
            self.processed_count += 1

            avg_temp = sum(temps) / len(temps) if temps else 0

            return (f"Sensor analysis: {len(data_batch)} readings "
                    f"processed, avg temp: {avg_temp:.1f}°C")
        except Exception as e:
            self.error_count += 1
            return f"Sensor processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            try:
                critical = [item for item in data_batch if 'temp' in
                            str(item) and float(str(item).split(':')[1]) > 30]
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
        self.total_transactions: int = 0
        self.net_flow: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            operations = 0
            flow = 0

            for item in data_batch:
                item_str = str(item)
                if 'buy' in item_str:
                    amount = int(item_str.split(':')[1])
                    flow -= amount
                    operations += 1
                elif 'sell' in item_str:
                    amount = int(item_str.split(':')[1])
                    flow += amount
                    operations += 1

            self.total_transactions += operations
            self.net_flow += flow
            self.processed_count += 1

            sign = '+' if flow >= 0 else ''
            return (f"Transaction analysis: {operations} operations, "
                    f"net flow: {sign}{flow} units")
        except Exception as e:
            self.error_count += 1
            return f"Transaction processing error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            try:
                large_trans = [
                        item for item in data_batch
                        if any(op in str(item) for op in ['buy', 'sell'])
                        and int(str(item).split(':')[1]) > 100
                ]
                return large_trans
            except Exception:
                return super().filter_data(data_batch, criteria)
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["total_transactions"] = self.total_transactions
        stats["net_flow"] = self.net_flow
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.total_events = 0
        self.error_events = 0

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
                    results.append(f"- {stream.stream_type}: {result}")
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
