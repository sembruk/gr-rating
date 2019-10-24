#!/usr/bin/env python3
import requests
import json
import re
from sfr_html_parser import SfrHtmlParser
from event_rating import EventRating, MainWeekendEventRating
from year_rating import YearRating
from html_generator import HtmlGenerator

def main():
    with open('urls.json') as urls_json_file:
        rogaines = json.load(urls_json_file)
        year_rating_men = YearRating()
        year_rating_women = YearRating()
        event_index = 0
        for rogaine in rogaines:
            print(rogaine['name'])
            year_rating_men.add_event(rogaine['name'])
            year_rating_women.add_event(rogaine['name'])
            urls = rogaine['url']
            if type(urls) != list:
                urls = [urls]
            participants = []
            for url in urls:
                r = requests.get(url)
                r.raise_for_status()

                sfr_html_parser = SfrHtmlParser()

                if re.search(r'windows-1251', r.text, flags=re.IGNORECASE):
                    r.encoding = 'cp1251'

                participants.append(sfr_html_parser.parse_results(r.text))

            participants_with_event_rating = None
            if event_index == 7:
                participants_with_event_rating = MainWeekendEventRating.calculate(participants)
            else:
                participants_with_event_rating = EventRating.calculate(participants[0])

            for p in participants_with_event_rating.values():
                if p.ismale():
                    year_rating_men.add_participant_event_rating(p)
                else:
                    year_rating_women.add_participant_event_rating(p)
            event_index += 1
        html_generator = HtmlGenerator(year_rating_men, year_rating_women)
        with open('/tmp/rating.html', 'w') as output_html_file:
            output_html_file.write(html_generator.html())

if __name__ == '__main__':
    main()

