from dataclasses import dataclass


class Generation:
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
