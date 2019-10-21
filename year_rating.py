from participant import Participant

class YearRating(object):

    def __init__(self):
        self.events = []
        self.participants = {}
        self.current_event_index = -1

    def add_event(self, event):
        self.events.append(event)
        self.current_event_index = len(self.events) - 1

    def add_participant_event_rating(self, participant: Participant):
        participant_year_rating = self.participants.setdefault(participant.hash(), {})
        participant_year_rating[self.current_event_index] = participant.get_rating()

    def print(self):
        for p in self.participants:
            #print(p, [self.participants[p][index] for index in self.participants[p]])
            print(p, self.participants[p])

