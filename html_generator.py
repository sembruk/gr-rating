from yattag import Doc
from year_rating import YearRating


class HtmlGenerator(object):

    def __init__(self, year_rating):
        doc, tag, text = Doc().tagtext()
        doc.asis('<!DOCTYPE html>')
        with tag('html'):
            with tag('head'):
                doc.stag('meta', ('http-equiv', 'Content-Type'), ('content', 'text/html; charset=utf-8'))
                with tag('style'):
                    text('table { border-collapse: collapse; } ')
                    text('table, td, th { border: 1px solid black; padding: 0 2px}')
#                    text('''
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
            with tag('body'):
                with tag('h1'):
                    text('GR Rating')
                with tag('h2'):
                    text('Group')
                with tag('table', ('border', '1')):
                    with tag('tr'):
                        with tag('th', klass='verticalTableHeader'):
                            with tag('p'):
                                text('Участник')
                        for h in year_rating.events:
                            with tag('th', klass='verticalTableHeader'):
                                with tag('p'):
                                    text(h)
                        with tag('th', klass='verticalTableHeader'):
                            with tag('p'):
                                text('Сумма')
                        with tag('th', klass='verticalTableHeader'):
                            with tag('p'):
                                text('Сумма 6')
                        with tag('th', klass='verticalTableHeader'):
                            with tag('p'):
                                text('Место')
                    participants = year_rating.sort_participants()
                    for i in range(len(participants)):
                        p = participants[i]
                        with tag('tr'):
                            with tag('td'):
                                text(p.participant_name_str)
                            for j in range(len(year_rating.events)):
                                with tag('td'):
                                    text(self.__class__.format_float(p.rating.get(j)))
                            with tag('td'):
                                text(self.__class__.format_float(p.get_sum()))
                            with tag('td'):
                                text(self.__class__.format_float(p.get_sum_of_6_results()))
                            with tag('td'):
                                text(i + 1)

        with open('/tmp/tmp.html', 'w') as output_html_file:
            output_html_file.write(doc.getvalue())

    @staticmethod
    def format_float(f):
        if f is None:
            return ''
        return '{:.1f}'.format(f)

