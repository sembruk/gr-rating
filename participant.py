from names.gender_by_name import GenderByName

class ParticipantBase(object):
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

    def ismale(self):
        return self.gender == 'm'


class Participant(ParticipantBase):
    
    def __init__(self, name, surname, year_of_birth, score, group):
        super().__init__(name, surname, year_of_birth)
        self.score = score
        self.group = group
        self.rating = 0

    def get_group(self):
        return self.group

    def get_score(self):
        return self.score

    def set_rating(self, rating):
        self.rating = rating

    def __str__(self):
        return super().__str__() + ' ' + ' '.join((self.group, str(self.score), '{:.2f}'.format(self.rating)))

