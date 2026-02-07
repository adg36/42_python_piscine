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
        if isinstance(data, dict):
            return data


class TransformStage:

    def process(self, data: Any) -> Dict:
        data_list = list(data.values())
        new_data = {}
        new_data[data_list[0]] = str(data_list[1]) + " " + data_list[2]
        return new_data


class OutputStage:

    def process(self, data: Any) -> str:
        line = ("Processed temperature reading: "
                "23.5°C (Normal range)")
        return line


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager:

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        if isinstance(pipeline, ProcessingPipeline):
            self.pipelines.append(pipeline)
        else:
            raise TypeError("Only ProcessingPipeline instances can be added")

    def process(self, data: Any) -> Any:
        for pipeline in self.pipelines:
            result = pipeline.process(data)
        return result


def main():
    # create NexusManager
    manager = NexusManager()

    # create pipelines
    json_pipeline = JSONAdapter("JSON_001")

    # configure pipelines with stages
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())

    # add pipelines to manager
    manager.add_pipeline(json_pipeline)

    # send data into manager
    raw_json = {"sensor": "temp", "value": 23.5, "unit": "C"}
    result = manager.process(raw_json)

    # manager selects pipeline

    # pipeline.process(data)

    # adapter preprocesses data

    # pipeline.run(data through stages)

    # adapter postprocesses result

    # result returned / printed
    print(result)


if __name__ == "__main__":
    main()
