#!/usr/bin/env python3
import requests
import json
from sfr_html_parser import SfrHtmlParser
from event_rating import EventRating

def main():
    with open('urls.json') as urls_json_file:
        rogaines = json.load(urls_json_file)
        for rogaine in rogaines:
            print(rogaine['name'])
            r = requests.get(rogaine['url'])
            r.raise_for_status()

            sfr_html_parser = SfrHtmlParser()
            r.encoding = 'cp1251'
            participants = sfr_html_parser.parse_results(r.text)
            event_rating = EventRating(participants)
            #event_rating.print()

if __name__ == '__main__':
    main()

