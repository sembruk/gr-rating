import json

class GenderByName(object):
    _gender_code = ('m', 'f')
    _names = None

    @classmethod
    def get_gender_by_name(cls, name):
        if cls._names is None:
            with open('names/names.json') as names_json_file:
                names_json_content = names_json_file.read()
                cls._names = json.loads(names_json_content)

        gender_index = cls._names[name]
        return cls._gender_code[gender_index]

