import csv
import json
import sys
import os
from dotenv import load_dotenv
import gspread
import category as cat
from time import sleep
import importcsv

# Link to google sheet
gc = gspread.service_account()
sh = gc.open("Budget Sheet")
wks = sh.worksheet("sheet 1")

transactions = []

# Insert data
with open('accounts.json') as f:
    accounts = json.load(f)
with open('titles.json') as f:
    titles = json.load(f)
key_cats = list(titles.keys())
with open('keywords.json') as f:
    keyword_list = json.load(f)
credit_cards = ('Visa', 'MasterCard', 'Amex')
NUMOFCAT = 0
for name in titles[key_cats[0]]:
    NUMOFCAT += 1
categories = []
for i in range(0, NUMOFCAT-1):
    for name in titles[key_cats[i+1]]:
        categories.append(cat.Category(titles[key_cats[0]][i], name))
keyword_dict = {}
i = 0
for keyword in keyword_list:
    keyword_dict.update({keyword : categories[i]})
    i += 1

def loadcsv():
    importcsv
    load_dotenv()
    PATH = os.environ.get("CSVFOLDER")
    file = PATH + f"/{sys.argv[1]}.csv"
    return file

def getTransactionDate(file, credit_cards=credit_cards):
    try:
        with open(file, mode='r') as csvf:
            reader = csv.reader(csvf)
            next(reader)
            for row in reader:
                try:
                    type = 'other'
                    card_used = ''
                    date = row[2]
                    desc = row[4][:19].lower()
                    vendor = row[4]
                    amount = row[6]
                    # Convert negative sign
                    if (amount.startswith('-')):
                        amount = amount.replace('-', '')
                    else:
                        amount = '-' + amount
                    category = 'Miscellaneous'
                    rate = ''
                    if row[0] in credit_cards:
                        type = 'Credit Card'
                        if row[1] in accounts[type]:
                            card_used = accounts[type][row[1]]
                            rate = accounts["cash back rate"][card_used][0]
                        # Set category and vendor
                        for keyword in keyword_dict:
                            if keyword in vendor:
                                category = keyword_dict[keyword].getCategory()
                                vendor = keyword_dict[keyword].getVendor()
                        if 'annual fee' in desc:
                            desc = card_used + ' Annual Fee'
                            vendor = 'Annual Fee'
                            type = 'Annual Fee'
                        # Record transaction
                        if category != 'Payment':
                            transaction = ((desc, vendor, category, float(amount), date, type, card_used, rate, float(amount)*float(rate), 0))
                            print(transaction)
                            transactions.append(transaction)
                except:
                    print("Error: Unable to extract data from csv file.")
        return transactions
    except:
        print("Error: Can't locate/open csv file.")

def main():
    file = loadcsv()
    entries = getTransactionDate(file)
    if entries is not None:
        for entry in entries:
            wks.insert_row(entry, 27)
            sleep(2)

main()