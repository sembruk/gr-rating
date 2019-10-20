#!/usr/bin/env python3
import requests
#from russiannames import NamesParser
from sfr_html_parser import SfrHtmlParser

def main():
    url = 'http://rogaining.msk.ru/protokol/Result_Tainstvenniy-Les_2019.htm'
    r = requests.get(url)
    r.raise_for_status()

    sfr_html_parser = SfrHtmlParser()
    sfr_html_parser.parse(r.text)

if __name__ == '__main__':
    main()

