from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class GenerationProtocol(Protocol):
    debug: str
    info: str
    warning: str
    error: str
    critical: str

    debug_tag: str
    info_tag: str
    warning_tag: str
    error_tag: str
    critical_tag: str


class Generation:
    def __post_init__(self):
        # Validate that the object conforms to the GenerationProtocol
        missing_fields = [
            attr for attr in GenerationProtocol.__annotations__
            if not hasattr(self, attr)
        ]
        if missing_fields:
            raise TypeError(
                f"Missing required fields for protocol conformance: {', '.join(missing_fields)}"
            )


@dataclass
class GenZ(Generation):
    debug: str = "yap"
    info: str = "deets"
    warning: str = "sketch"
    error: str = "sus"
    critical: str = "cooked"

    debug_tag: str = "JUST YAPPING"
    info_tag: str = "SPILLING SOME DEETS"
    warning_tag: str = "THAT'S SKETCH"
    error_tag: str = "SOMETHING IS SUS"
    critical_tag: str = "SYSTEM IS COOKED"
