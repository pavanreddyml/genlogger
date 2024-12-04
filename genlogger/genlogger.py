import logging
from .generations import Generation
from typing import Type, TypeVar

T = TypeVar("T", bound=Generation)

class GenLogging:
    def __new__(cls, generation: Type[T], *args, **kwargs) -> logging.Logger:
        target_logging = logging

        if generation is None:
            raise ValueError("Generation must be provided")
        
        dataclass = generation()
        
        # Set custom logging level tags
        target_logging.addLevelName(target_logging.DEBUG, dataclass.debug_tag)
        target_logging.addLevelName(target_logging.INFO, dataclass.info_tag)
        target_logging.addLevelName(target_logging.WARNING, dataclass.warning_tag)
        target_logging.addLevelName(target_logging.ERROR, dataclass.error_tag)
        target_logging.addLevelName(target_logging.CRITICAL, dataclass.critical_tag)

        # Dynamically create methods based on dataclass mappings
        def create_method(level_name, method_name):
            def method(self, message, *args, **kwargs):
                self.log(level_name, message, *args, **kwargs)
            return method

        # Map dataclass attributes to logging levels
        # Will dict {GenZ level: Real Logging Level}
        level_mapping = {
            getattr(dataclass, 'debug', 'debug'): target_logging.DEBUG,
            getattr(dataclass, 'info', 'info'): target_logging.INFO,
            getattr(dataclass, 'warning', 'warning'): target_logging.WARNING,
            getattr(dataclass, 'error', 'error'): target_logging.ERROR,
            getattr(dataclass, 'critical', 'critical'): target_logging.CRITICAL,
        }

        # Add level constants (eg: logging.YAP == logging.DEBUG for GenZ and so on)
        for attr_name, level_name in level_mapping.items():
            upper_name = attr_name.upper()
            setattr(target_logging, upper_name, level_name)

        # Add methods to the logging module (eg: logging.yap, logging.deets, for GenZ)
        # for method_name, level_name in level_mapping.items():
        #     def log_method(message, level=level_name, *args, **kwargs):
        #         target_logging.log(level, message, *args, **kwargs)
        #     setattr(target_logging, method_name, log_method)

        # Patch the Logger class to include the new methods
        # This is to that the logger also has all the methods for the generation
        # example: logger.yap, logger.deets, for GenZ
        # Without this, the methods will only work for logging (logging.yap) but not for logger (logger.yap)
        original_logger_class = logging.getLoggerClass()

        class GenLogger(original_logger_class):
            pass

        for method_name, level_name in level_mapping.items():
            method = create_method(level_name, method_name)
            setattr(GenLogger, method_name, method)

        logging.setLoggerClass(GenLogger)

        return target_logging