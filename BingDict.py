import requests
import sys
from bs4 import BeautifulSoup

def search(keyword):
    payload = {'q': keyword}
    r = requests.get('https://cn.bing.com/dict/search',params=payload)
    soup = BeautifulSoup(r.text)
    metas = soup.find_all("meta")
    for meta in metas:
       if meta['name'] == 'description':
          pos = meta['content'].find('，')
          desp = meta['content'][pos + 1:]
          return desp
    return ''

if __name__ == '__main__':
 if len(sys.argv) < 2:
     print("error")
 else :
    desc = search(sys.argv[1])
    print(desc)