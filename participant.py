
class Participant(object):
    #names_parser = NamesParser()

    def __init__(self, name, surname, year_of_birth):
        self.name = name.title()
        self.surname = surname.title()
        self.year_of_birth = year_of_birth
        self.gender = 'm'
    
    def hash(self):
        return '_'.join((self.name, self.surname, self.year_of_birth))

    def __str__(self):
        return ' '.join((self.name, self.surname, self.year_of_birth))

    #def parse_name(self, name, surname):
    #    result = names_parser.parse(name)
    #    if result['parsed']:
    #        return Participant(
    #            name,
    #            surname,
    #            result.gender)
        

class ParticipantWithScore(Participant):
    
    def __init__(self, name, surname, year_of_birth, score):
        super().__init__(name, surname, year_of_birth)
        self.score = score

