import re
import operator
from participant import Participant
    
class KindRating(object):
    
    def __init__(self, id_):
        self.id = id_
        self.participants = {}

    def add_participant(self, participant: Participant):
        self.participants[participant.hash()] = participant

    def calculate_rating(self):
        max_score = max(self.participants.values(), key=operator.methodcaller('get_score')).get_score()
        for p in self.participants.values():
            p.set_rating(p.get_score()*100/max_score)

    def get_participants(self):
        return self.participants
        
    def __str__(self):
        ret_str = ''
        return '\n'.join([str(p) for p in self.participants])


class EventRating(object):

    @classmethod
    def calculate(cls, participants):
        rating = {}
        for participant in participants:
            kind = cls.extract_rogaining_kind(participant.get_group())
            if participant.ismale():
                kind += '_m'
            else:
                kind += '_f'
            kind_rating = rating.setdefault(kind, KindRating(kind))
            kind_rating.add_participant(participant)

        all_participants = {}
        for kind in rating:
            rating[kind].calculate_rating()
            all_participants.update(rating[kind].get_participants())
        return all_participants

    @staticmethod
    def extract_rogaining_kind(group):
        match_result = re.match(r'[\w-]+[\d.,]+(\w)', group)
        try:
            return match_result.group(1)
        except (AttributeError, IndexError):
            raise Exception('Unknown group name: %s' % group)


