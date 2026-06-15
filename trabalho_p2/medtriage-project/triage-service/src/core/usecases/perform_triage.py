from src.core.domain.entities import Triage, TriageStrategy
from src.core.usecases.interfaces import TriageRepository

class PerformTriageUseCase:
    def __init__(self, repository: TriageRepository, strategy: TriageStrategy):
        self.repository = repository
        self.strategy = strategy

    def execute(self, triage: Triage) -> Triage:
        triage.classify(self.strategy)
        self.repository.save(triage)
        return triage