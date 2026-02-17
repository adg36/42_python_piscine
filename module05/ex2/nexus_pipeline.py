#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol


class ProcessingStage(Protocol):
    
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


class InputStage:

    def process(self, data: Any) -> Dict:
        print(f"Input: {data}")
        if isinstance(data, dict):
            return data
        else:
            data_dict = {}
            data_dict["data"] = data
            return data_dict


class TransformStage:

    def process(self, data: Any) -> Dict:
        if "value" in data.keys():
            value = data["value"]
            status = "Normal range" if 15 <= value <= 30 else "Critical"
            enriched = {**data, "status": status}
            print(f"Transform: Enriched with metadata and validation")
            return enriched
        elif "data" in data.keys():
            if "," in data:
                data = data.split(",")
                print("Transform: Parsed and structured data")
            else:
                print("Transform: Aggregated and filtered")
            return data


class OutputStage:

    def process(self, data: Any) -> str:
        sensor = data.get("sensor", "unknown")
        value = data.get("value", 0)
        status = data.get("status", "Unknown status")
        line = (f"Output: Processed {sensor} reading: "
                f"{value}°C ({status})")
        print(line)
        return line


class JSONAdapter(ProcessingPipeline):
    data_type = "json"

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing JSON data through pipeline...")
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    data_type = "csv"

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing CSV data through same pipeline...")
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    data_type = "stream"

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing Stream data through same pipeline...")
        return super().process(data)


def detect_data_type(data: Any) -> str:
    if isinstance(data, dict):
        return "json"
    elif isinstance(data, str) and "," in data:
        return "csv"
    else:
        return "stream"


class NexusManager:

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        if isinstance(pipeline, ProcessingPipeline):
            self.pipelines.append(pipeline)
        else:
            raise TypeError("Only ProcessingPipeline instances can be added")

    def process(self, data: Any) -> Any:
        data_type = detect_data_type(data)
        for pipeline in self.pipelines:
            if pipeline.data_type == data_type:
                result = pipeline.process(data)
            else:
                print(f"No pipeline registered for {data_type}")
        return result


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    # create NexusManager
    manager = NexusManager()
    print("Initializing Nexus Manager...\n"
          "Pipeline capacity: 1000 streams/second\n")

    # create pipelines
    pipelines = [
            JSONAdapter("JSON_001"),
            CSVAdapter("CSV_001"),
            StreamAdapter("Stream_001")
    ]

    # configure pipelines with stages and add them to manager
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    
    print("\n=== Multi-Format Data Processing ===")
    
    for pipeline in pipelines:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        manager.add_pipeline(pipeline)
    
    data = [{"sensor": "temp", "value": 23.5, "unit": "C"},
            "user,action,timestamp",
            "Real-time sensor stream"
    ]

    for batch in data:
        result = manager.process(batch)
        print(result)


if __name__ == "__main__":
    main()
