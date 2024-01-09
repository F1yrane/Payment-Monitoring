import json
from operator import itemgetter


def get_transactions(file):
    """Opening JSON File"""
    with open(file, 'r', encoding='utf-8') as transactions:
        transactions_list = json.loads(transactions.read())
        return transactions_list


def get_executed_transactions(transactions_list):
    """Getting Successful Transactions"""
    executed_transactions = list()
    for transaction in transactions_list:
        if len(transaction) > 0 and transaction['state'] == 'EXECUTED':
            executed_transactions.append(transaction)

    return executed_transactions


def get_last_five_transactions(transactions_list):
    "Getting The Last Five Transactions"""
    transactions_list.sort(key=itemgetter('date'))
    last_five_transactions = list()
    for transaction in reversed(transactions_list[-5:]):
        last_five_transactions.append(transaction)

    return last_five_transactions


