from flask import Flask, request, jsonify
import my_grpc
import my_grpc.service_pb2 as service_pb2

CERTIFICATE_PATH = "./certs/server.crt"

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    location = data.get("location")
    date_range = data.get("date_range")

    with open(CERTIFICATE_PATH, "rb") as cert_file:
        credentials = my_grpc.ssl_channel_credentials(cert_file.read())

    with my_grpc.secure_channel(, credentials) as channel:
        stub = service_pb2_grpc.DiseasePredictionServiceStub(channel)
        response = stub.PredictOutbreak(service_pb2.OutbreakRequest(
            location=location,
            date_range=date_range
        ))
        return jsonify({
            "location": response.location,
            "prediction": response.prediction,
            "confidence": response.confidence,
            "recommendations": response.recommendations
        })

if __name__ == "__main__":
    app.run(ssl_context=('certs/server.crt', 'certs/server.key'))
