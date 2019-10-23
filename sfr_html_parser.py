import re
from lxml import html
from participant import *

class SfrHtmlParser(object):
    
    def __init__(self):
        pass

    def parse_results(self, html_string):
        tree = html.fromstring(html_string)
        h2_nodes = tree.xpath('//h2')
        self.participants = []
        for h2_node in h2_nodes:
            group_name = h2_node.text

            surname_tableindex = None
            name_tableindex = None
            year_of_birth_tableindex = None
            score_tableindex = None

            table_node = h2_node.xpath('.//following::table')[0]
            table_row_nodes = table_node.xpath('.//tbody/tr')
            if not table_row_nodes:
                table_row_nodes = table_node.xpath('.//tr')
            table_header = table_row_nodes[0].xpath('.//th')
            for i in range(len(table_header)):
                th_text = table_header[i].text
                if re.match(r'Фамилия', th_text, flags=re.IGNORECASE):
                    surname_tableindex = i
                elif re.match(r'Имя', th_text, flags=re.IGNORECASE):
                    name_tableindex = i
                elif re.match(r'Г.р.', th_text, flags=re.IGNORECASE):
                    year_of_birth_tableindex = i
                elif re.match(r'\*\*\*', th_text, flags=re.IGNORECASE):
                    score_tableindex = i

            table_row_nodes = table_row_nodes[1:]
            for tr_node in table_row_nodes:
                td_nodes = tr_node.xpath('.//td')
                surname = self.__class__.get_td_text(td_nodes[surname_tableindex])
                name = self.__class__.get_td_text(td_nodes[name_tableindex])
                year_of_birth = self.__class__.get_td_text(td_nodes[year_of_birth_tableindex])
                score_str = (self.__class__.get_td_text(td_nodes[score_tableindex]) or ['0'])[0]
                #if self.__class__.int_or_null(score_str) < 0:
                #    score_str = self.__class__.get_td_text(td_nodes[7])[0]
                score = self.__class__.int_or_null(score_str)
                for i in range(len(surname)):
                    self.participants.append(Participant(self.__class__.first_word(name[i]), surname[i], year_of_birth[i], score, group_name))
        return self.participants

    @staticmethod
    def get_td_text(td_node):
        return td_node.xpath('.//nobr[1]/text()')

    @staticmethod
    def int_or_null(s):
        try:
            return int(s)
        except ValueError as ve:
            if s == '-':
                return 0
            return -1

    @staticmethod
    def first_word(s):
        return s.split(None, 1)[0]



