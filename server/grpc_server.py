import grpc
from concurrent import futures
import grpc.service_pb2_grpc as service_pb2_grpc
from loguru import logger

from my_grpc import service_pb2


class DiseasePredictionService(service_pb2_grpc.DiseasePredictionServiceServicer):
    def PredictOutbreak(self, request, context):
        logger.info(f"Received request for location: {request.location}, date range: {request.date_range}")

        # Mock prediction logic (replace with real logic later)
        prediction = "High Risk" if "New York" in request.location else "Low Risk"
        confidence = "0.85" if prediction == "High Risk" else "0.75"
        recommendations = "Increase hygiene measures" if prediction == "High Risk" else "Maintain current measures"

        return service_pb2.OutbreakResponse(
            location=request.location,
            prediction=prediction,
            confidence=confidence,
            recommendations=recommendations
        )


class YourService:
    pass


def serve():
    server = my_grpc.server()
    your_service_pb2_grpc.add_YourServiceServicer_to_server(YourService(), server)
    address = 'd164b5720ad8431da315c3a690eac207'
    server.add_insecure_port(address)
    print(f"Server is running on https://mainnet.infura.io/v3/d164b5720ad8431da315c3a690eac207")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":    serve()
