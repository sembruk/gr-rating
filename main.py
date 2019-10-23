#!/usr/bin/env python3
import requests
import json
import re
from sfr_html_parser import SfrHtmlParser
from event_rating import EventRating
from year_rating import YearRating
from html_generator import HtmlGenerator

def main():
    with open('urls.json') as urls_json_file:
        rogaines = json.load(urls_json_file)
        year_rating_men = YearRating()
        year_rating_women = YearRating()
        for rogaine in rogaines:
            print(rogaine['name'])
            year_rating_men.add_event(rogaine['name'])
            year_rating_women.add_event(rogaine['name'])
            r = requests.get(rogaine['url'])
            r.raise_for_status()

            sfr_html_parser = SfrHtmlParser()

            if re.search(r'windows-1251', r.text, flags=re.IGNORECASE):
                r.encoding = 'cp1251'

            participants = sfr_html_parser.parse_results(r.text)
            participants_with_event_rating = EventRating.calculate(participants)
            for p in participants_with_event_rating:
                if p.ismale():
                    year_rating_men.add_participant_event_rating(p)
                else:
                    year_rating_women.add_participant_event_rating(p)
        #year_rating_men.print()
        html_generator = HtmlGenerator(year_rating_men)

if __name__ == '__main__':
    main()

