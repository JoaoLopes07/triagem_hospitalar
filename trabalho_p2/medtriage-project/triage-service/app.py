from flask import Flask, request, jsonify
from src.core.domain.entities import Triage, ManchesterStrategy
from src.infrastructure.database.repository import MemoryTriageRepository
from src.core.usecases.perform_triage import PerformTriageUseCase

app = Flask(__name__)
repository = MemoryTriageRepository()
strategy = ManchesterStrategy()

@app.route("/triage", methods=["POST"])
def create_triage():
    data = request.json
    triage = Triage(
        triage_id=data["triage_id"],
        patient_id=data["patient_id"],
        oxygen=data["oxygen"],
        heart_rate=data["heart_rate"]
    )
    use_case = PerformTriageUseCase(repository, strategy)
    updated_triage = use_case.execute(triage)
    
    return jsonify({
        "triage_id": updated_triage.triage_id,
        "patient_id": updated_triage.patient_id,
        "color": updated_triage.color,
        "status": updated_triage.status
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)