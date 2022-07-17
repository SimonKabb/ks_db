import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'cred.json')

CREDENTIALS_FILE = 'cred.json'
spreadsheet_id = '1gmOeYU2Z-UL5RAfBxNgaecCfjMdM9bvLi5knCqVqNjs'


def read_table(spreadsheet_id, CREDENTIALS_FILE):
    '''Чтение данных из таблицы, 
    возвращает данные в формате list[list1,list2,..]'''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=httpAuth)
    sheet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='Лист1',
        majorDimension='ROWS').execute()
    values = sheet['values']
    return values


if __name__ == '__main__':
    print(read_table(spreadsheet_id, CREDENTIALS_FILE))
