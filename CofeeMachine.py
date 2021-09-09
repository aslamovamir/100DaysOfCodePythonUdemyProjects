# Author:                 Amir Aslamov
# Description of Project: This project is designed to simulate the digital version
#                         of a simple coffee machine with some drink types available
#                         and is operated on coins.
# Date of Creation:       /started: Aug 29, 2021, at 10:07 PM EST, Florida, U.S. /
#                         /finished:  /Aug 30, 2021, at 02:33 PM EST, Florida, U.S. /


import data


def resource_check(client_choice, resource_available):

    if client_choice == 'espresso':
        return ((resource_available['water'] - data.MENU['espresso']['ingredients']['water'] < 0) or
                (resource_available['coffee'] - data.MENU['espresso']['ingredients']['coffee'] < 0))
    elif client_choice == 'latte':
        return ((resource_available['water'] - data.MENU['latte']['ingredients']['water'] < 0) or
                (resource_available['coffee'] - data.MENU['latte']['ingredients']['coffee'] < 0) or
                (resource_available['milk'] - data.MENU['latte']['ingredients']['milk'] < 0))
    elif client_choice == 'cappuccino':
        return ((resource_available['water'] - data.MENU['cappuccino']['ingredients']['water'] < 0) or
                (resource_available['coffee'] - data.MENU['cappuccino']['ingredients']['coffee'] < 0) or
                (resource_available['milk'] - data.MENU['cappuccino']['ingredients']['milk'] < 0))


def transaction_process(num_quarters, num_dimes, num_nickels, num_pennies, drink_choice):

    total_inserted = round((0.25 * num_quarters + 0.10 * num_dimes + 0.05 * num_nickels + 0.01 * num_pennies), 2)
    # print(f"TOTAL INSERTED: {total_inserted}")

    # print("HERE IS THE COST OF THE CHOICE DRINK: ")
    # if drink_choice == 'espresso':
    #     print(data.MENU['espresso']['cost'])
    #     print(f"HERE IS THE CHANGE: {total_inserted - data.MENU['espresso']['cost']}")
    # elif drink_choice == 'latte':
    #     print(data.MENU['latte']['cost'])
    #     print(f"HERE IS THE CHANGE: {total_inserted - data.MENU['latte']['cost']}")
    # elif drink_choice == 'cappuccino':
    #     print(data.MENU['cappuccino']['cost'])
    #     print(f"HERE IS THE CHANGE: {total_inserted - data.MENU['cappuccino']['cost']}")

    # checking if total inserted is less than the cost of the drink chosen by the client
    # first, we find out the type of the drink, then we check the funds
    if drink_choice == 'espresso':
        if total_inserted < data.MENU['espresso']['cost']:
            print("Transaction failure! Sorry, insufficient funds. Money refunded.")
            return -1
        else:
            change = round((total_inserted - data.MENU['espresso']['cost']), 2)
            print(f"Transaction success! Here's your ${change} in change.")
            return total_inserted - change
    elif drink_choice == 'latte':
        if total_inserted < data.MENU['latte']['cost']:
            print('Transaction failure! Sorry, insufficient funds. Money refunded.')
            return -1
        else:
            change = round((total_inserted - data.MENU['latte']['cost']), 2)
            print(f"Transaction success! Here's your ${change} in change.")
            return total_inserted - change
    elif drink_choice == 'cappuccino':
        if total_inserted < data.MENU['cappuccino']['cost']:
            print('Transaction failure! Sorry, insufficient funds. Money refunded.')
            return -1
        else:
            change = round((total_inserted - data.MENU['cappuccino']['cost']), 2)
            print(f"Transaction success! Here's your ${change} in change.")
            return total_inserted - change


def machine_flow():

    machine_resources = data.resources

    # creating a new field to store the total profit of the machine, with an initial amount of 0
    machine_resources['profit'] = 0

    flow_stop = False

    # taking user reply
    while not flow_stop:
        client_choice = input("What would you like today? (espresso/latte/cappuccino): ").lower()

        # analyzing the user's choice
        if client_choice == 'espresso' or client_choice == 'latte' or client_choice == 'cappuccino':
            flow_stop = resource_check(client_choice, machine_resources)
            if flow_stop:
                print("Sorry, no sufficient resources for this drink.")
                flow_stop = False
                continue
            else:
                num_quarters = int(input("Number of quarters: "))
                num_dimes = int(input("Number of dimes: "))
                num_nickels = int(input("Number of nickels: "))
                num_pennies = int(input("Number of pennies: "))
                transaction_profit = round((transaction_process(num_quarters, num_dimes, num_nickels,
                                            num_pennies, client_choice)), 2)

                if transaction_profit == -1:
                    # print("NOT ENOUGH MONEY!")
                    continue
                else:
                    machine_resources['profit'] += transaction_profit

                    # subtracting the ingredient amount of the drink choice from the machine resources accordingly
                    if client_choice == 'espresso':
                        machine_resources['water'] -= data.MENU['espresso']['ingredients']['water']
                        machine_resources['coffee'] -= data.MENU['espresso']['ingredients']['coffee']
                    elif client_choice == 'latte':
                        machine_resources['water'] -= data.MENU['latte']['ingredients']['water']
                        machine_resources['milk'] -= data.MENU['latte']['ingredients']['milk']
                        machine_resources['coffee'] -= data.MENU['latte']['ingredients']['coffee']
                    elif client_choice == 'cappuccino':
                        machine_resources['water'] -= data.MENU['cappuccino']['ingredients']['water']
                        machine_resources['milk'] -= data.MENU['cappuccino']['ingredients']['milk']
                        machine_resources['coffee'] -= data.MENU['cappuccino']['ingredients']['coffee']

                    # print("PRINTING THE MACHINE RESOURCES OBJECT:")
                    # print(machine_resources)
                    continue

        elif client_choice == 'off':
            print("Machine turned OFF")
            flow_stop = True
        elif client_choice == 'report':
            print(machine_resources)
            continue
        else:
            print("Input unrecognized! Please try again.")


# MAIN
machine_flow()
