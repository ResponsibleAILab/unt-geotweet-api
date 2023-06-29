import requests
import json
from typing import Tuple, List
from datetime import date

def get_num_str(num: int):
    return str(num) if num > 9 else f'0{num}'

def get_date_str(date: date) -> str:
    return f'{date.year}-{get_num_str(date.month)}-{get_num_str(date.day)}'

base_url = 'https://sigspatial.yunhefeng.me/api'

def get_by_tweet_location(
        region: str, 
        country: str, 
        language: str, 
        start: date, 
        end: date
    ) -> List[int]:
    query = f'\
?from_date={get_date_str(start)}\
&to_date={get_date_str(end)}\
&region={region}\
&country={country}\
&language={language}'
    res = requests.get(f'{base_url}/query_tweet_location.php{query}')
    if res.status_code != 200:
        print(res)
        return []
    data = json.loads(res.content)
    return [int(item) for item in data]

def get_by_user_location(
        city: str, 
        country: str, 
        language: str, 
        start: date, 
        end: date
    ) -> List[int]:
    query = f'\
?from_date={get_date_str(start)}\
&to_date={get_date_str(end)}\
&city={city}\
&country={country}\
&language={language}'
    res = requests.get(f'{base_url}/query_tweet_location.php{query}')
    if res.status_code != 200:
        print(res)
        return []
    data = json.loads(res.content)
    return [int(item) for item in data]

def get_by_coordinates(
        point: Tuple[float, float], 
        distance: int, 
        language: str, 
        start: date, 
        end: date
    ) -> List[int]:
    query = f'\
?from_date={get_date_str(start)}\
&to_date={get_date_str(end)}\
&distance={distance}\
&latitude={point[0]}\
&longitude={point[1]}\
&language={language}'
    res = requests.get(f'{base_url}/query_coordinates.php{query}')
    if res.status_code != 200:
        print(res)
        return []
    data = json.loads(res.content)
    return [int(item) for item in data]