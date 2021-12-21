import pandas
import datetime
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your_gspread_credentials.json", scope)
client = gspread.authorize(creds)
lead_sheet = client.open("sheet_name").worksheet("worksheet_name")

a = lead_sheet.get_all_records()
df = pd.DataFrame(a)
df['row'] = df.reset_index().index
df.to_json('your_file_name.json', orient='records', indent=2 )
