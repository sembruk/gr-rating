import re
from participant import Participant
    
class KindRating(object):
    
    def __init__(self, id_):
        self.id = id_
        self.participants = []

    def add_participant(self, participant: Participant):
        self.participants.append(participant)

    def sort(self):
        self.participants.sort(reverse=True, key=lambda p: p.get_score())

    def calculate_rating(self):
        max_score = self.participants[0].get_score()
        for p in self.participants:
            p.set_rating(p.get_score()*100/max_score)
        
    def __str__(self):
        ret_str = ''
        return '\n'.join([str(p) for p in self.participants])


class EventRating(object):

    def __init__(self, participants):
        self.rating = {}
        for participant in participants:
            kind = self.__class__._extract_rogaining_kind(participant.get_group())
            if participant.ismale():
                kind += '_m'
            else:
                kind += '_f'
            kind_rating = self.rating.setdefault(kind, KindRating(kind))
            kind_rating.add_participant(participant)

    def print(self):
        for kind in self.rating:
            print(kind)
            self.rating[kind].sort()
            self.rating[kind].calculate_rating()
            print(self.rating[kind])


    @staticmethod
    def _extract_rogaining_kind(group):
        match_result = re.match(r'[\w-]+[\d.,]+(\w)', group)
        try:
            return match_result.group(1)
        except (AttributeError, IndexError):
            raise Exception('Unknown group name: %s' % group)

