import requests
import sys
def search(keyword):
    payload = {'q': keyword}
    r = requests.get('https://cn.bing.com/dict/search',params=payload)
    data=r.text
    start=data.find('<meta name="description"')
    start=start+46+len(keyword)
    end=data.find('" />',start)

    return data[start:end]

if __name__ =='__main__':
 if len(sys.argv)<2:
     print("error")
 else :
    desc=search(sys.argv[1])
    print(desc)