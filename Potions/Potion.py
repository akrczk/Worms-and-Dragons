from abc import ABC, abstractmethod


class Potion(ABC):
    duration: int | None = None
    statistic_field: str | None = None

    @abstractmethod
    def apply(self):
        pass

    @staticmethod
    def get_display_name():
        return ""
