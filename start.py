from Core.main import get_transactions, get_executed_transactions, get_last_five_transactions, \
    get_date_of_transaction, masking_of_transfer_data


def run():
    """Launching The Program"""
    transactions = get_transactions('Data/transactions.json')
    executed_transactions = get_executed_transactions(transactions)
    last_five_operations = get_last_five_transactions(executed_transactions)
    for operation in last_five_operations:
        if 'from' in operation.keys():
            return(f"{get_date_of_transaction(operation)} {operation['description']}\n"
                  f"{masking_of_transfer_data(operation['from'])} -> "
                  f"{masking_of_transfer_data(operation['to'])}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
        else:
            return(f"{get_date_of_transaction(operation)} {operation['description']}\n"
                  f"{masking_of_transfer_data(operation['to'])}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")


print(run())