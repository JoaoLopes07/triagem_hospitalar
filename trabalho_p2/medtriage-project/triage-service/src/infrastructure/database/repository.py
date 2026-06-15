from src.core.domain.entities import Triage
from src.core.usecases.interfaces import TriageRepository

class MemoryTriageRepository(TriageRepository):
    def __init__(self):
        self.db = {}

    def save(self, triage: Triage) -> None:
        self.db[triage.triage_id] = triage

    def find_by_id(self, triage_id: str) -> Triage:
        return self.db.get(triage_id)