import requests
import os


def weather_api():
    CWB_API_KEY = os.getenv('CWB_API_KEY')

    if not CWB_API_KEY:
        print("API_KEY not found")
        return
    
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    parmas = {
        'Authorization': CWB_API_KEY,
        'locationName': '臺北市',
    }

    res = requests.get(url, params=parmas)
    data = res.json()
    return data
