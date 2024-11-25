commands = {
    "main": {
        "organizations": (lambda: list_organizations(), "Print a list of organization IDs from Registry"),
        "services": (lambda: list_services_for_org(), "Print a list of service IDs for an organization"),
        "balance": (lambda: print_balance(), "Print account and escrow balances"),
        "deposit": (lambda: deposit(), "Deposit AGIX tokens into MPE"),
        "block": (lambda: print_block_number(), "Print the current Ethereum block number"),
        "channel": (lambda: switch_to_menu("channel"), "Go to the channel menu"),
        "help": (lambda: commands_help(), "Print the list of available commands"),
        "exit": (lambda: exit(0), "Exit the application")
    },
    "channel": {
        "update": (lambda: update_channels(), "Update the list of initialized payment channels"),
        "list": (lambda: list_channels(), "Print the list of payment channels"),
        "open": (lambda: open_channel(), "Open a new payment channel"),
        "help": (lambda: commands_help(), "Print the list of available commands"),
        "back": (lambda: switch_to_menu("main"), "Return to the main menu"),
        "exit": (lambda: exit(0), "Exit the application")
    }
}

active_commands = commands["main"]


def main():
    global active_commands
    print("Hello, welcome to the Snet SDK console application!")
    print("To use the application, type the name of the command you want to execute.")
    commands_help()
    prefix = ">>> "

    while True:
        command = input(prefix).strip()
        if command in active_commands:
            active_commands[command][0]()
        else:
            print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")
def list_organizations():
    print("Organizations:")
    org_list = snet_sdk.get_organization_list()
    for org in org_list:
        print(f"- {org}")
def list_services_for_org():
    org_id = input("Enter organization ID: ").strip()
    print("Services:")
    services = snet_sdk.get_services_list(org_id=org_id)
    for service in services:
        print(f"- {service}")
def print_balance():
    balance = snet_sdk.account.balance()
    escrow_balance = snet_sdk.account.escrow_balance()
    print(f"Account balance: {balance}")
    print(f"Escrow balance: {escrow_balance}")
def open_channel():
    global active_service
    if not active_service:
        print("No active service selected!")
        return
    amount = int(input("Enter amount of AGIX tokens (in cogs): "))
    expiration = int(input("Enter expiration time (in blocks): "))
    channel = active_service.open_channel(amount=amount, expiration=expiration)
    channels.append(channel)
    print("Payment channel opened successfully!")
def switch_to_menu(menu_name):
    global active_commands
    active_commands = commands[menu_name]
    commands_help()
def commands_help():
    print("Available commands:")
    for command, details in active_commands.items():
        print(f"- {command}: {details[1]}")
if __name__ == "__main__":
    main()
