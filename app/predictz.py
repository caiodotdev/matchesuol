

import datetime
import http
import time
from bs4 import BeautifulSoup
from requests import request
import requests

from app.engine import EngineModel
from app.models import Match, Time
from django.db.models import Q


class PredictZ(EngineModel):

    URI = 'http://www.predictz.com/predictions/'
    HEADERS = {
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.predictz.com",
        "referer": 'https://www.predictz.com/',
    }

    def get_info(self, args, **kwargs):
        return self.get_matches()

    def _time_normal(self, time_name):
        time_name = time_name.lower()
        qs = Time.objects.filter(nome_comum__icontains=time_name)
        if qs.exists():
            return qs.first()
        else:
            return None

    def get_match_on_db(self, time1, time2):
        time1_obj = self._time_normal(time1)
        time2_obj = self._time_normal(time2)
        today = datetime.datetime.now()
        matches = Match.objects.filter(data=today.date())
        if time1_obj:
            qs = matches.filter(time1=time1_obj)
        else:
            qs = matches.filter(time2=time2_obj)
        if qs.exists():
            return qs.first()
        return None

    def update_match_on_db(self, time1, time2, predict_score, predict_result):
        # match = self.get_match_on_db(time1, time2)
        # print('match: ' + str(match))
        # if match:
        #     match.predict_score = predict_score
        #     match.predict_result = predict_result
        #     # match.save()
        #     print('updated: ' + str(match))
        # else:
        #     print('not found')
        pass

    def get_matches(self):
        matches_founded = []
        self.browser.get(self.URI)
        time.sleep(5)
        html = self.browser.page_source
        page = BeautifulSoup(html, 'html.parser')
        matches = page.find_all('div', {'class': 'pttr ptcnt'})
        print('founded: ' + str(len(matches)))
        for match in matches:
            result_tag = match.find('div', {'class': 'ptpredboxsml'})
            if result_tag:
                result_match = result_tag.text.split(' ')
                predict_score = result_match[1]
                predict_result = str(result_match[0])
                if predict_result == 'Home' or predict_result == 'Away':
                    predict_result = predict_result + ' Win'
                a_tag = match.find('div', {'class': 'pttd ptgame'}).find('a')
                dispute = a_tag.text
                divisor = dispute.index(' v ')
                time1 = dispute[:divisor]
                time2 = dispute[divisor+3:]
                matches_founded.append({'dispute': dispute, 'time1': time1, 'time2': time2,
                                        'predict_score': predict_score, 'predict_result': predict_result})
                self.update_match_on_db(
                    time1, time2, predict_score, predict_result)
        self.dispose()
        return matches_founded
