
class Participant(object):

    def __init__(self, name, surname, gender, year_of_birth=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.year_of_birth = year_of_birth
    
    def set_year_of_birth(self, year_of_birth):
        self.year_of_birth = year_of_birth

    def hash(self):
        separator = '_'
        return separator.join(self.name, self.surname, self.year_of_birth)

