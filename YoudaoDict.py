import requests
import sys
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

def search(keyword):
    payload = {}
    r = requests.get('http://youdao.com/w/eng/' + keyword, params=payload)
    data = r.text
    start = data.find('<div id="phrsListTab"')
    start = data.find('<ul>', start)
    end = data.find('</ul>', start)

    start = data.find('<li>', start, end)
    desc = ''
    while start != -1:
        current_end = data.find('</li>', start, end)
        desc += data[start + 4:current_end] + '\n'
        start = data.find('<li>', current_end, end)

    return desc


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error")
    else:
        desc = search(sys.argv[1])
        print(desc)
