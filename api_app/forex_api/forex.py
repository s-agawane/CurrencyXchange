import requests

def forex_rate(base_cur, dest_cur, date_obj='latest'):
    source_url = "https://api.ratesapi.io/api/"

    payload = {'base': base_cur, 'symbols': dest_cur, 'rtype': 'fpy'}
    source_url = source_url + date_obj
    response = requests.get(source_url, params=payload)
    if response.status_code == 200:
        rate = response.json().get('rates')
        if not rate:
            return 'apidown'
        return rate[dest_cur]
    return '404'
