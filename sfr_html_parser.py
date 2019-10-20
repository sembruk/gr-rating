from russiannames import NamesParser
import participant

class SfrHtmlParser(object):
    names_parser = NamesParser()
    
    def __init__(self):
        pass

    def parse_name(self, name, surname):
        result = names_parser.parse(name)
        if result['parsed']:
            return Participant(
                name,
                surname,
                result.gender)

    def parse_year_of_birth(self, participant, yob_string):
        year_of_birth = int(yob_string)
        participant.set_year_of_birth(year_of_birth)

    def parse_score(self, score_string):
        return int(score_string)
        


