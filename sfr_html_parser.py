from lxml import html
from participant import *

class SfrHtmlParser(object):
    
    def __init__(self):
        pass

    def parse(self, html_string):
        tree = html.fromstring(html_string)
        h2_nodes = tree.xpath('//h2')
        self.participants = {}
        for h2_node in h2_nodes:
            group_name = h2_node.text
            group = []

            table_row_nodes = h2_node.xpath('.//following::table[1]/tr')[1:]
            for tr_node in table_row_nodes:
                td_nodes = tr_node.xpath('.//td')
                surname = self.__class__.get_td_text(td_nodes[2])
                name = self.__class__.get_td_text(td_nodes[3])
                year_of_birth = self.__class__.get_td_text(td_nodes[4])
                score = self.__class__.int_or_null(self.__class__.get_td_text(td_nodes[6])[0])
                for i in range(len(surname)):
                    group.append(ParticipantWithScore(self.__class__.first_word(name[i]), surname[i], year_of_birth[i], score))
            
            self.participants[group_name] = group
        return self.participants

    @staticmethod
    def get_td_text(td_node):
        return td_node.xpath('.//nobr[1]/text()')

    @staticmethod
    def int_or_null(s):
        try:
            return int(s)
        except ValueError as ve:
            return 0

    @staticmethod
    def first_word(s):
        return s.split(None, 1)[0]



