import requests
import sys
from bs4 import BeautifulSoup


def search(keyword):
    payload = {}
    r = requests.get('http://youdao.com/w/eng/' + keyword, params=payload)
    soup = BeautifulSoup(r.text)
    ul=soup.find(id="phrsListTab").ul
    desc=''
    for li in ul.find_all("li"):
        desc+=li.string+'\n'
    return desc


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error")
    else:
        desc = search(sys.argv[1])
        print(desc)
