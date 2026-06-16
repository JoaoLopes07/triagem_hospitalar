from flask import Flask, request, jsonify

app = Flask(__name__)

patients_db = {}

@app.route("/patients", methods=["POST"])
def register_patient():
    data = request.json
    patient_id = data["patient_id"]
    patients_db[patient_id] = data
    return jsonify(data), 201

@app.route("/patients/<patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = patients_db.get(patient_id)
    if not patient:
        return jsonify({"message": "Paciente nao encontrado"}), 404
    return jsonify(patient), 200

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "servico": "Microsservico de Pacientes (Patient-Service)",
        "status": "Online"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
