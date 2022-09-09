import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path


class GoogleSheet:
    TITLE_NAME = 'test_list!A1:D1'
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

    def get_title(self):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.TITLE_NAME).execute()
        values = result.get('values', [])
        return values

    def get_values(self):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
        values = result.get('values', [])
        return values
