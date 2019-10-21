#!/usr/bin/env python3
import requests
import re
from sfr_html_parser import SfrHtmlParser
from participant import Participant

def extract_rogaining_kind(group):
    match_result = re.match(r'[\w-]+[\d.,]+(\w)', group)
    try:
        return match_result.group(1)
    except (AttributeError, IndexError):
        raise Exception('Unknown group name: %s' % group)
    
class EventRatingForKind(object):
    
    def __init__(self, id_):
        self.id = id_
        self.male = []
        self.female = []

    def add_participant(self, participant: Participant):
        if participant.ismale():
            self.male.append(participant)
        else:
            self.female.append(participant)

    def sort(self):
        self.male.sort(reverse=True, key=lambda participant: participant.get_score())
        self.female.sort(reverse=True, key=lambda participant: participant.get_score())

    def __str__(self):
        ret_str = ''
        for m in self.male:
            ret_str += str(m) + '\n'
        ret_str += '\n'
        for f in self.female:
            ret_str += str(f) + '\n'

        return ret_str


def main():
    #url = 'http://rogaining.msk.ru/protokol/Result_Tainstvenniy-Les_2019.htm'
    #url = 'http://rogaining.msk.ru/protokol/Result_Pozdnaya_Osen_2019.htm'
    #url = 'http://rogaining.msk.ru/protokol/Result_MosDen_2019.htm'
    url = 'http://rogaining.msk.ru/protokol/Result-Zimniy-Rogaining-2019.htm'
    r = requests.get(url)
    r.raise_for_status()

    sfr_html_parser = SfrHtmlParser()
    participants = sfr_html_parser.parse_results(r.text)

    rogaining_kinds = {}
    eventRating = {}
    for participant in participants:
        kind = extract_rogaining_kind(participant.get_group())
        eventRatingForKind = eventRating.setdefault(kind, EventRatingForKind(kind))
        eventRatingForKind.add_participant(participant)
        #grop_list = rogaining_kinds.setdefault(kind, [])
        #grop_list.append(group)

    for kind in eventRating:
        print(kind)
        eventRating[kind].sort()
        print(eventRating[kind])
    #for key in rogaining_kinds:
    #    print(key)
    #    print(rogaining_kinds[key])

if __name__ == '__main__':
    main()

