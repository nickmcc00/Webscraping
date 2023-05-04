from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font
import keys
from twilio.rest import Client



url = 'https://www.coingecko.com/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)


tables = soup.findAll('table')
updated_tables = tables[0]
rows = updated_tables.findAll('tr')


client = Client(keys.accountSID, keys.authToken)

#TwilioNumber = "+15075167290"

#mycellphone = "+18322312653"

TwilioNumber = ""

mycellphone = ""


wb = xl.Workbook()
ws = wb.active
ws.title = "Cryptocurrencies"

ws['A1'] = "Number"
ws['B1'] = "Cryptocurrency"
ws['C1'] = "Price"
ws['D1'] = "Percent change within 24 hours"
ws['E1'] = "Price based on change"

header_font = Font(size=14, bold=True)

ws['A1'].font = header_font
ws['B1'].font = header_font
ws['C1'].font = header_font
ws['D1'].font = header_font
ws['E1'].font = header_font



wb.save("Cryptocurrencies.xlsx")