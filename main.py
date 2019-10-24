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

            participants_with_event_rating = EventRating.calculate(participants[0])

            # Multiday event
            #if len(urls) > 1: 
            #    per_list = [participants_with_event_rating]
            #    for i in range(1, len(urls)):
            #        per_list.append(EventRating.calculate(participants[i]))

            #    all_per_set = set()
            #    for per in per_list:
            #        all_per_set.update(set(per))

            #    for p_hash in all_per_set:
            #        p = per_list[0][p_hash]
            #        p_score_sum = None
            #        p_kind = None
            #        # 'Главный Weekend' rules
            #        for per in per_list:
            #            p = per.get(p_hash)
            #            if p is not None:
            #                if p_kind is None:
            #                    p_kind = EventRating.extract_rogaining_kind(p.get_group())
            #                    p_score_sum = p.get_score()
            #                if EventRating.extract_rogaining_kind(p.get_group()) != p_kind:
            #                    p_score_sum += p.get_score()
            #                    p.set_score(p_score_sum)


            for p in participants_with_event_rating.values():
                if p.ismale():
                    year_rating_men.add_participant_event_rating(p)
                else:
                    year_rating_women.add_participant_event_rating(p)
        #year_rating_men.print()
        html_generator = HtmlGenerator(year_rating_men)

if __name__ == '__main__':
    main()

