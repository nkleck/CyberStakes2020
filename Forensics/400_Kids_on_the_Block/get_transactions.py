#!/usr/bin/env python3
from web3 import Web3, HTTPProvider
import json
import csv

'''
We are going to grab each of the transactions from the chain, and save them as a csv file.
This will make importing into maltego simple
'''

# Connection to the remote server
w3 = Web3(HTTPProvider('http://localhost:8545'))

# get stqrting position
latest = w3.eth.getBlock('latest', full_transactions=True)
# print(Web3.toJSON(latest))

# get all of the transactions
current_block = latest['number']
transaction_list = []
while current_block >= 0:
    # get the block
    block = w3.eth.getBlock(current_block, full_transactions=True)
    # iterate over list of transactions in the block
    for transaction in block['transactions']:
        sub_transaction = {}
        sub_transaction['blockNumber'] = transaction['blockNumber']
        sub_transaction['from'] = transaction['from']
        sub_transaction['to'] = transaction['to']
        transaction_list.append(sub_transaction)

    # decrement block
    current_block = current_block - 1

# convert list of dict's to a csv
with open('transactions.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=transaction_list[0].keys(),)
    dict_writer.writeheader()
    dict_writer.writerows(transaction_list)

print('done')
