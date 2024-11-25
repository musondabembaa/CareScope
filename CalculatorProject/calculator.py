from snet import sdk
config = {
    "private_key": "<d164b5720ad8431da315c3a690eac207>",  # Replace with your private key
    "eth_rpc_endpoint": "https://mainnet.infura.io/v3/d164b5720ad8431da315c3a690eac207",  # Replace with your API key
    "concurrency": False,
    "identity_name": "My First key",
    "identity_type": "d164b5720ad8431da315c3a690eac207",
    "network": "Ethereum",
    "force_update": False
}

import snet.sdk

calc_client = snet.sdk.create_service_client(
    org_id="Phoetrek",
    service_id="risk-aware-assessment",
    group_name="default"
)
def parse_expression(expression):
    elements = list(expression.split())
    if len(elements) != 3:
        raise Exception(f"Invalid expression '{expression}'. Three items required.")
    a = float(elements[0])  # Allow both integers and decimals
    b = float(elements[2])
    if elements[1] not in ["+", "-", "*", "/"]:
        raise Exception(f"Invalid operation '{elements[1]}'. Allowed: +, -, *, /")
    return a, b, elements[1]
operators = {
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "div"
}
def main():
    print("""
    Welcome to the calculator powered by SingularityNET platform!
    Please type the expression you want to calculate, e.g. 2 + 3.
    Type 'exit' to exit the program.
    """)
    while True:
        expression = input("Calculator> ")
        if expression.lower() == "exit":
            break
        try:
            a, b, op = parse_expression(expression)
            print(f"Calculating {a} {op} {b}...")
            result = calc_client.call_rpc(operators[op], "Numbers", a=a, b=b)
            print(f"{a} {op} {b} = {result}")
        except Exception as e:
            print("Error:", e)
if __name__ == "__main__":
    main()
