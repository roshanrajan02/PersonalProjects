import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header
    'Connection'      : 'close'
}

statistics_url = 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'
profile_url = 'https://finance.yahoo.com/quote/{}/profile?p={}'
financials_url = 'https://finance.yahoo.com/quote/{}/financials?p={}'

stock = input("Enter a stock ticker:")

response = requests.get(financials_url.format(stock, stock), headers=headers, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]
start = script_data.find("context")-2
json_data = json.loads(script_data[start:-12])
annual_is = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
annual_cf = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
annual_bs = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']

#income statement data
annual_is_stmts = []

for stmt in annual_is:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val['raw']
        except TypeError: 
            continue
        except KeyError:
            continue
    annual_is_stmts.append(statement)
print("Annual Income Statements:")
for is_stmt in annual_is_stmts:
    print(is_stmt)

#profile data 
response = requests.get(profile_url.format(stock, stock), headers=headers, timeout=5)
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text=pattern).contents[0]
json_data = json.loads(script_data[start:-12])
businessSummary = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['assetProfile']['longBusinessSummary']
secFilings = json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['secFilings']['filings']
print("Business Summary:")
print(businessSummary)
print("Previous SEC Filings:")
print(secFilings)
