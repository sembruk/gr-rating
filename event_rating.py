import re
import operator
from participant import Participant
    
class KindRating(object):
    
    def __init__(self, id_=''):
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


class MainWeekendGenderRating(KindRating):

    def add_participant(self, p: Participant):
        p_hash = p.hash()
        if self.participants.get(p_hash) is None:
            self.participants[p_hash] = p
        else:
            self.participants[p_hash].inc_score(p.get_score())

    def calculate_rating(self):
        super().calculate_rating()
        for p in self.participants.values():
            print(p)



class MainWeekendEventRating(EventRating):

    @classmethod
    def calculate(cls, subevents):
        subevent_day1_participants = subevents[0]
        subevent_day2_participants = subevents[1]

        rating_men = MainWeekendGenderRating()
        rating_women = MainWeekendGenderRating()

        kinds = ['Б', 'В']

        for day_index in range(len(subevents)):
            p_list_without_duplicates = {p.hash(): p for p in subevents[day_index]}.values()

            for participant in p_list_without_duplicates:
                kind = cls.extract_rogaining_kind(participant.get_group())
                if kind == kinds[day_index]:
                    if participant.ismale():
                        rating_men.add_participant(participant)
                    else:
                        rating_women.add_participant(participant)
        rating_men.calculate_rating()
        rating_women.calculate_rating()
        all_participants = {}
        all_participants.update(rating_men.get_participants())
        all_participants.update(rating_women.get_participants())
        return all_participants

