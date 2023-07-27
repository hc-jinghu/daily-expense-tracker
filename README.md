# About
This program utilized Selenium to automate csv downloading and record transactions to your google sheet. 

## Prerequistites:
Your online banking doesn't offer an API to capture this information.

```NOTE: If your bank has an API, use that instead```

## How to use:
### .csv Download Automation
Setup bank account credentials and sign-in page URL in your `.env`, then run `getTransactioncsv.py`.
This script is for RBC online bank, your online banking UI may look different. If so, make adjustments to suit yours. 
```This doesn't work for all banks, some bank block bot activities. If that's the case, manually download the csv file from your bank. ```

### Record Transaction to Google Sheet
Using Google API. [Access google sheet using gspread library.](https://docs.gspread.org/en/v5.10.0/)
Setup account details in your `accounts.json`, then run `transactions.py`.
Make sure `.csv` file are in the correct directory.
