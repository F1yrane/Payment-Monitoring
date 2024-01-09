import json
import re

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


def get_date_of_transaction(transaction):
    "Correct Date Display"""
    date = transaction["date"][:10].replace("-", ".")
    date = '.'.join(reversed(date.split('.')))
    return date


def masking_of_transfer_data(transaction):
    """Hiding Data"""
    nums = ''.join(re.findall(r'\d+', transaction))
    name_of_card = ''.join(re.findall(r'\D+', transaction))

    if nums[16:20]:
        nums = nums.replace(nums[6:-4], '**********')
        nums = ''.join([nums[14:20]])
        return f'{name_of_card}{nums}'
    else:
        nums = nums.replace(nums[6:-4], '******')
        nums = ' '.join([nums[:4], nums[4:8], nums[8:12], nums[12:16]])
        return f'{name_of_card}{nums}'
    