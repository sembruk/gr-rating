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
            with tag('body'):
                with tag('h1'):
                    text('GR Rating')
                with tag('h2'):
                    text('Group')
                with tag('table'):
                    with tag('tr'):
                        with tag('th'):
                            text('Участник')
                        for h in year_rating.events:
                            with tag('th'):
                                text(h)
                        with tag('th'):
                            text('Сумма')
                        with tag('th'):
                            text('Сумма 6')
                        with tag('th'):
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

