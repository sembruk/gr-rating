from names.gender_by_name import GenderByName

class Participant(object):
    #names_parser = NamesParser()

    def __init__(self, name, surname, year_of_birth):
        self.name = name.title()
        self.surname = surname.title()
        self.year_of_birth = year_of_birth
        self.gender = GenderByName.get_gender_by_name(self.name)
    
    def hash(self):
        return '_'.join((self.name, self.surname, self.year_of_birth))

    def __str__(self):
        return ' '.join((self.name, self.surname, self.year_of_birth, self.gender))


class ParticipantWithScore(Participant):
    
    def __init__(self, name, surname, year_of_birth, score):
        super().__init__(name, surname, year_of_birth)
        self.score = score

