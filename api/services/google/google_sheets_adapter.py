import requests
import json
from settings import Settings


class GoogleSheetsAdapter:
    def __init__(self, sheet_id, sheet_range):
        self.sheet_id = sheet_id
        self.sheet_range = sheet_range
        key = Settings.get_api_key()
        self.url = Settings.get_api_url() + '/spreadsheets/' + sheet_id + '/values/' + sheet_range + '?key=' + key

    def call(self):
        api_response = requests.get(self.url)

        if api_response.status_code != 200:
            error_result = dict()
            error_result['status_code'] = api_response.status_code
            error_result['message'] = 'There was an error calling the API'
            error_result['error'] = api_response.json()
            print api_response.json()
            return json.dumps(error_result)

        else:
            result_json = api_response.json()
            clean_result = dict()
            values = result_json['values']
            print values
            headers = values[0]
            clean_result['headers'] = headers
            list_length = len(values)
            clean_result['total_rows'] = list_length - 1 if list_length > 0 else list_length
            data = []
            for val in values[1:list_length]:
                print val
                row = dict()
                for i, v in enumerate(headers):
                    row[headers[i]] = val[i] if i < len(val) else ''
                data.append(row)

            clean_result['data'] = data
            return json.dumps(clean_result)
