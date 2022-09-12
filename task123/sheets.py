import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import requests
from datetime import datetime
import xml.etree.ElementTree as ET


class Sheets:
    RANGE_NAME = 'test_list!A2:D100000000'
    SPREADSHEET_ID = '1edkilV72I8LS0M2y-xcQTAsBWejvDS5xzkFljIs_yos'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('task123/token.pickle'):
            with open('task123/token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'task123/credentials.json', self.SCOPES)
                print(flow)
                creds = flow.run_local_server(port=0)
            with open('task123/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def get_exchange_rate(self):
        url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={datetime.today().strftime("%d/%m/%Y")}'
        response = requests.get(url)
        tree = ET.fromstring(response.content)
        unit_rate = None
        for rate in tree.findall("./Valute[@ID='R01235']/Value"):
            unit_rate = rate.text
        return unit_rate.replace(',', '.')

    def get_data(self):
        data = []
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
        values = tuple(result.get('values', []))
        for money in values:
            rate = float(money[2]) * float(self.get_exchange_rate())
            money.append(round(rate, 1))
            data.append(tuple(money))
        return tuple(data)

