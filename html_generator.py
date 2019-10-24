from yattag import Doc
from year_rating import YearRating


class HtmlGenerator(object):

    def __init__(self, year_rating_men, year_rating_women):
        self.doc, self.tag, self.text = Doc().tagtext()

        title = 'Рейтинг кубка «Золотой маршрут 2019»'
        self.doc.asis('<!DOCTYPE html>')
        with self.tag('html'):
            with self.tag('head'):
                self.doc.stag('meta', ('http-equiv', 'Content-Type'), ('content', 'text/html; charset=utf-8'))
                with self.tag('style'):
                    self.text('table { border-collapse: collapse; } ')
                    self.text('table, td, th { border: 1px solid black; padding: 0 2px}')
#                    self.text('''
#.verticalTableHeader {
#    text-align:center;
#    white-space:nowrap;
#    g-origin:50% 50%;
#    -webkit-transform: rotate(270deg);
#    -moz-transform: rotate(270deg);
#    -ms-transform: rotate(270deg);
#    -o-transform: rotate(270deg);
#    transform: rotate(270deg);
#    
#}
#.verticalTableHeader p {
#    margin:0 -100% ;
#    display:inline-block;
#}
#.verticalTableHeader p:before{
#    content:'';
#    width:0;
#    padding-top:110%;/* takes width as reference, + 10% for faking some extra padding */
#    display:inline-block;
#    vertical-align:middle;
#}
#table {
#    text-align: center;
#    table-layout: fixed;
#    width: 950px
#}''')
                with self.tag('title'):
                    self.text(title)
            with self.tag('body'):
                with self.tag('h1'):
                    self.text(title)
                group_names = ('Мужчины', 'Женщины')
                self._generate_refs(group_names, 0)
                self._generate_table(year_rating_men, group_names[0])
                self._generate_refs(group_names, 1)
                self._generate_table(year_rating_women, group_names[1])

        self._html = self.doc.getvalue()

    def html(self):
        return self._html

    def _generate_refs(self, group_names, index):
        self.doc.stag('br')
        self.doc.stag('a', ('name', group_names[index]))
        for gn in group_names:
            with self.tag('a', ('href', '#' + gn)):
                self.text(gn)
            self.doc.asis('\t')

    def _generate_table(self, year_rating, group_name):
        with self.tag('h2'):
            self.text(group_name)
        with self.tag('table', ('border', '1')):
            with self.tag('tr'):
                with self.tag('th', klass='verticalTableHeader'):
                    with self.tag('p'):
                        self.text('Участник')
                for h in year_rating.events:
                    with self.tag('th', klass='verticalTableHeader'):
                        with self.tag('p'):
                            self.text(h)
                with self.tag('th', klass='verticalTableHeader'):
                    with self.tag('p'):
                        self.text('Сумма')
                with self.tag('th', klass='verticalTableHeader'):
                    with self.tag('p'):
                        self.text('Сумма 6')
                with self.tag('th', klass='verticalTableHeader'):
                    with self.tag('p'):
                        self.text('Место')
            participants = year_rating.sort_participants()
            for i in range(len(participants)):
                p = participants[i]
                with self.tag('tr'):
                    with self.tag('td'):
                        self.text(p.participant_name_str)
                    for j in range(len(year_rating.events)):
                        with self.tag('td'):
                            self.text(self.__class__.format_float(p.rating.get(j)))
                    with self.tag('td'):
                        self.text(self.__class__.format_float(p.get_sum()))
                    with self.tag('td'):
                        self.text(self.__class__.format_float(p.get_sum_of_6_results()))
                    with self.tag('td'):
                        self.text(i + 1)


    @staticmethod
    def format_float(f):
        if f is None:
            return ''
        return '{:.1f}'.format(f)

