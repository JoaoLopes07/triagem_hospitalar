import unittest
from src.core.domain.entities import Triage, ManchesterStrategy
from src.infrastructure.database.repository import MemoryTriageRepository
from src.core.usecases.perform_triage import PerformTriageUseCase

class TestTriageProcess(unittest.TestCase):

    def test_should_classify_as_emergency_when_oxygen_is_critical(self):
        triage = Triage(triage_id="tr-001", patient_id="pt-100", oxygen=80, heart_rate=130)
        repository = MemoryTriageRepository()
        strategy = ManchesterStrategy()
        use_case = PerformTriageUseCase(repository, strategy)

        result = use_case.execute(triage)

        self.assertEqual(result.color, "VERMELHO")
        self.assertEqual(result.status, "CLASSIFICADO")
        self.assertEqual(repository.find_by_id("tr-001").color, "VERMELHO")

    def test_should_classify_as_yellow_when_oxygen_is_mildly_low(self):
        triage = Triage(triage_id="tr-002", patient_id="pt-101", oxygen=90, heart_rate=80)
        repository = MemoryTriageRepository()
        strategy = ManchesterStrategy()
        use_case = PerformTriageUseCase(repository, strategy)

        result = use_case.execute(triage)

        self.assertEqual(result.color, "AMARELO")

    def test_should_classify_as_green_when_vital_signs_are_normal(self):
        triage = Triage(triage_id="tr-003", patient_id="pt-102", oxygen=98, heart_rate=75)
        repository = MemoryTriageRepository()
        strategy = ManchesterStrategy()
        use_case = PerformTriageUseCase(repository, strategy)

        result = use_case.execute(triage)

        self.assertEqual(result.color, "VERDE")

if __name__ == "__main__":
    unittest.main()