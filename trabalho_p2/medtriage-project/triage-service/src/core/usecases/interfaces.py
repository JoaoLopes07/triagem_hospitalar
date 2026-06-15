from abc import ABC, abstractmethod
from src.core.domain.entities import Triage

class TriageRepository(ABC):
    @abstractmethod
    def save(self, triage: Triage) -> None:
        pass

    @abstractmethod
    def find_by_id(self, triage_id: str) -> Triage:
        pass