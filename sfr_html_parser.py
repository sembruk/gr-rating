from lxml import html
from participant import Participant

class SfrHtmlParser(object):
    
    def __init__(self):
        pass

    def parse(self, html_string):
        tree = html.fromstring(html_string)
        h2_node = tree.xpath('//h2')[5]
        print(h2_node.text)
        table_row_nodes = h2_node.xpath('.//following::table[1]/tr')[1:]
        for tr_node in table_row_nodes:
            td_nodes = tr_node.xpath('.//td')
            surname = self.__class__.get_td_text(td_nodes[2])
            name = self.__class__.get_td_text(td_nodes[3])
            year_of_birth = self.__class__.get_td_text(td_nodes[4])
            score = self.__class__.int_or_null(self.__class__.get_td_text(td_nodes[6]))
            print(Participant(name, surname, year_of_birth), score)

    @staticmethod
    def get_td_text(td_node):
        return td_node.xpath('.//nobr')[0].text

    @staticmethod
    def int_or_null(s):
        try:
            return int(s)
        except ValueError as ve:
            return 0



