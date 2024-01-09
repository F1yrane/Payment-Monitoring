from Core.main import get_transactions, get_executed_transactions, get_last_five_transactions


def run():
    """Launching The Program"""
    transactions = get_transactions('Data/transactions.json')
    executed_transactions = get_executed_transactions(transactions)
    last_five_operations = get_last_five_transactions(executed_transactions)

run()