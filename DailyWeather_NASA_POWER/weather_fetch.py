# import required modules
import os, json, requests
import pandas as pd
from typing import List
import datetime


def fetch_temp_json(location: List, base_url: str, start: datetime, end: datetime):
    """

    :param location:
    :param base_url:
    :param start:
    :param end:
    :return:
    """
    output = r""

    for latitude, longitude in location:
        api_request_url = base_url.format(longitude=longitude, latitude=latitude, start=start, end=end)
        response = requests.get(url=api_request_url, verify=True, timeout=30.00)
        content = json.loads(response.content.decode('utf-8'))

        filename = response.headers['content-disposition'].split('filename=')[1]
        print(filename)
        filepath = os.path.join(output, filename)
        with open(filepath, 'w') as file_object:
            json.dump(content, file_object)

    return output


def temp_to_df(json_file: str):
    """

    :param json_file:
    :return:
    """
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the data you want into a dictionary
    rows = []
    for date, values in data['properties']['parameter']['T2M'].items():
        row = {
            'date': date,
            'T2M': values,
            'PRECTOTCORR': data['properties']['parameter']['PRECTOTCORR'][date],
            'T2M_MAX': data['properties']['parameter']['T2M_MAX'][date],
            'T2M_MIN': data['properties']['parameter']['T2M_MIN'][date],
        }
        rows.append(row)

    # Convert the dictionary to a DataFrame and save as CSV
    df = pd.DataFrame(rows, columns=['date', 'T2M', 'PRECTOTCORR', 'T2M_MAX', 'T2M_MIN'])
    # df.to_csv('data.csv', index=False)
    print(df.head())
    print(df.info())

    return df


#

if __name__ == '__main__':
    locations = [(40.7128, -74.0060), (5, 10)]
    base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,PRECTOTCORR,T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start={start}&end={end}&format=JSON"
    start_date = 20230101
    end_date = 20230331

    # fetch_temp_json(location=locations, base_url=base_url, start=start_date, end=end_date)

    temp_to_df(json_file='POWER_Point_Daily_20230101_20230331_040d71N_074d01W_LST.json')
