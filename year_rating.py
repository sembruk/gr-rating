from participant import Participant

class ParticipantYearRating(object):
    
    def __init__(self, participant_name_str):
        self.participant_name_str = participant_name_str
        self.rating = {}
        self.sum = 0
        self.sum_of_6_results = None

    def add_event_rating(self, event_index, event_rating):
        self.rating[event_index] = event_rating
        self.sum += event_rating

    def get_n_events(self):
        return len(self.rating)

    def get_sum(self):
        return self.sum

    def get_sum_of_6_results(self):
        sorted_rating_list = sorted(self.rating.values(), reverse=True)[0:6]
        self.sum_of_6_results = sum(sorted_rating_list)
        return self.sum_of_6_results


class YearRating(object):

    def __init__(self):
        self.events = []
        self.participants = {}
        self.current_event_index = -1

    def add_event(self, event):
        self.events.append(event)
        self.current_event_index = len(self.events) - 1

    def add_participant_event_rating(self, participant: Participant):
        participant_year_rating = self.participants.setdefault(participant.hash(), ParticipantYearRating(participant.hash()))
        participant_year_rating.add_event_rating(self.current_event_index, participant.get_rating())

    def sort_participants(self):
        s = self.participants.values()
        s = sorted(s, reverse=True, key=lambda p: p.get_sum())
        s = sorted(s, reverse=True, key=lambda p: p.get_n_events())
        s = sorted(s, reverse=True, key=lambda p: p.get_sum_of_6_results())
        return s

    def print(self):
        l = self.sort_participants()
        for p in l:
            print(p.participant_name_str, p.get_sum_of_6_results(), p.get_n_events(), p.get_sum())

