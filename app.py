from flask import Flask, request
from api.services.google.google_sheets_adapter import GoogleSheetsAdapter


app = Flask(__name__)


@app.route('/')
def hello_world():
    sheet_id = request.args['sheet_id']  # '1h1YVNLPOVIAjCt082T-GIkKppq_iDTyudOrYSmLTCiM'
    sheet_range = request.args['range']  # 'Sheet1A1:E59'
    adapter = GoogleSheetsAdapter(sheet_id, sheet_range).call()
    return adapter


if __name__ == '__main__':
    app.run(debug=True)
