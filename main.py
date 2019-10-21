#!/usr/bin/env python3
import requests
from sfr_html_parser import SfrHtmlParser
from event_rating import EventRating

def main():
    #url = 'http://rogaining.msk.ru/protokol/Result_Tainstvenniy-Les_2019.htm'
    #url = 'http://rogaining.msk.ru/protokol/Result_Pozdnaya_Osen_2019.htm'
    #url = 'http://rogaining.msk.ru/protokol/Result_MosDen_2019.htm'
    url = 'http://rogaining.msk.ru/protokol/Result-Zimniy-Rogaining-2019.htm'
    r = requests.get(url)
    r.raise_for_status()

    sfr_html_parser = SfrHtmlParser()
    participants = sfr_html_parser.parse_results(r.text)
    event_rating = EventRating(participants)
    event_rating.print()

if __name__ == '__main__':
    main()

