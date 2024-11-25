from snet import sdk
from config import config  # Import the config file
# Initialize the SDK
snet_sdk = sdk.SnetSDK(config)

# Create a service client for the Example Service
org_id = "Photrek"
service_id = "risk-aware-assessment"
group_name = "default_group"
service_client = snet_sdk.create_service_client(org_id, service_id, group_name)
result = service_client.call_rpc("mul", "Numbers", a=20, b=3)
print(f"Performing 20 * 3: {result}")  # Expected output: value: 60.0
