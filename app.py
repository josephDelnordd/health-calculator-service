from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200


@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()

    try:
        height = float(data["height"])
        weight = float(data["weight"])
        bmi_value = calculate_bmi(height, weight)
        return jsonify({"bmi": bmi_value}), 200

    except (KeyError, TypeError):
        return jsonify({"error": "height and weight are required"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/bmr", methods=["POST"])
def bmr():
    data = request.get_json()

    try:
        height = float(data["height"])
        weight = float(data["weight"])
        age = int(data["age"])
        gender = data["gender"]

        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": bmr_value}), 200

    except (KeyError, TypeError):
        return jsonify({"error": "height, weight, age and gender are required"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)