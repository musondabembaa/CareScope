import my_grpc
import adr_pb2 as adr_pb2
import adr_pb2_grpc as adr_pb2_grpc

def run_client():
    with my_grpc.insecure_channel('https://mainnet.infura.io/v3/d164b5720ad8431da315c3a690eac207') as channel:
        stub = adr_pb2_grpc.DiseasePredictionServiceStub(channel)
        response = stub.PredictOutbreak( adr_pb2_grpc.OutbreakRequest(
            location="New York",
            date_range="2024-01-01 to 2024-01-31"
        ))
        print("Response from server:")
        print(f"Location: {response.location}")
        print(f"Prediction: {response.prediction}")
        print(f"Confidence: {response.confidence}")
        print(f"Recommendations: {response.recommendations}")

if __name__ == "__main__":
    run_client()
