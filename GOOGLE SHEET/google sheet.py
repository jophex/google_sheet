from __future__ import print_function


import gspread
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
# SERVICE_ACCOUNT_FILE = 'alphapent9060-21779ed67a40.json'

# creds = None
credentials = service_account.Credentials.from_service_account_file(
    'alphapent9060-21779ed67a40.json', scopes=SCOPES)

client = gspread.authorize(credentials)

# 1NArTpkQZEKzpVWB-GuseZWVB3CkPVM-V0hPm65AZgrI

SAMPLE_SPREADSHEET_ID = '1NArTpkQZEKzpVWB-GuseZWVB3CkPVM-V0hPm65AZgrI'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# service = build('sheets', 'v4', credentials=creds)


sheet = client.open("alphapent9060").sheet1
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                           # range="sheet1!A1:C5").execute()
# values = result.get('values', [])

data = sheet.update_cell(1, 1, "joseph")

#data = sheet.delete_row(1)
#data = sheet.get_values()
print(data)
