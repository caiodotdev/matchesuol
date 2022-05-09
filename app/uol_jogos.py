import http

import requests

HEADERS = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'pt-BR, pt;q=0.9, en-US;q=0.8, en;q=0.7',
           'Cache-Control': 'no-cache',
           'Connection': 'keep - alive',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'cross-site',
           'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


class UolAPI():
    def __init__(self):
        self.url = 'https://www.uol.com.br/esporte/service/?loadComponent=match-service&contentType=json'

    def get_matches(self):
        req = requests.get(self.url, headers=HEADERS)
        if req.status_code == http.HTTPStatus.OK:
            return req.json()['matches']
        return None
