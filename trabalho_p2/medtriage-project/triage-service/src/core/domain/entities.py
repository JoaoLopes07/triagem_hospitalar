from abc import ABC, abstractmethod

class TriageStrategy(ABC):
    @abstractmethod
    def evaluate(self, oxygen_saturation: int, heart_rate: int) -> str:
        pass

class ManchesterStrategy(TriageStrategy):
    def evaluate(self, oxygen_saturation: int, heart_rate: int) -> str:
        if oxygen_saturation < 85 or heart_rate > 120:
            return "VERMELHO"
        if oxygen_saturation < 95:
            return "AMARELO"
        return "VERDE"

class Triage:
    def __init__(self, triage_id: str, patient_id: str, oxygen: int, heart_rate: int):
        self.triage_id = triage_id
        self.patient_id = patient_id
        self.oxygen = oxygen
        self.heart_rate = heart_rate
        self.status = "PENDENTE"
        self.color = "VERDE"

    def classify(self, strategy: TriageStrategy):
        self.color = strategy.evaluate(self.oxygen, self.heart_rate)
        self.status = "CLASSIFICADO"