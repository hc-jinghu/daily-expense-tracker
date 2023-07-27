import gspread
import csv
import json
import os
from dotenv import load_dotenv

load_dotenv()
PATH = "csv6407.csv" #TODO: change this to taking argv[1] instead

with open('accounts.json') as f:
    accounts = json.load(f)

path = f"{PATH}"
transactions = []
markets = ['HMART', 'METRO', 'WHOLE FOODS', 'T&T', 'SHOPPERS']
foodDelivery = ['DOORDASH', 'EATS']
transits = ['PRESTO', 'TRIP']
subscriptions = ['']
credit_cards = ['Visa', 'MasterCard', 'Amex']


def getTransactionData(path, markets=markets, foodDelivery=foodDelivery, transits=transits):
    try:
        with open(path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            res = 1
            try:
                for row in csv_reader:
                    type = ''
                    card_used = ''
                    date = row[2]
                    desc = row[4]
                    amount = row[6]
                    category = 'Misc'
                    if row[0] in credit_cards:
                        type = 'Credit Card'
                    if row[1] in accounts[type]:
                        card_used = accounts[type][str(row[1])]
                    while res == 1:
                        for market in markets:
                            if market in desc:
                                category = 'Groceries'
                                res = 0
                                break
                        for foodDel in foodDelivery:
                            if foodDel in desc:
                                category = 'Food Delivery'
                                res = 0
                                break
                        for transit in transits:
                            if transit in desc:
                                category = 'Transportation'
                                res = 0
                                break
                        if 'FEE' in desc:
                            category = 'Fee'
                            break
                        if 'FREEDOM MOBILE' in desc:
                            category = 'Phone Bill'
                            break
                        if 'PAYMENT' in desc:
                            category = 'Payment'
                            break
                        break
                    res = 1
                    transaction = ((date, desc, category, amount, type, card_used))
                    print(transaction)
                    transactions.append(transaction)
                return transactions
            except:
                print("Fail to extract data from csv file.")
    except:
        print("CSV file cannot be opened.")

# gc = gspread.service_account()
# sh = gc.open("Transactions sheet")
# wks = sh.worksheet()

rows = getTransactionData(path)
