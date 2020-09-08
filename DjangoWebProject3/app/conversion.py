import requests
import math
from bs4 import BeautifulSoup


def bitcoin_conversion():
    r =requests.get('https://finance.yahoo.com/quote/BTCUSD%3DX?p=BTCUSD%3DX')
    #print(r.text[0:500])
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('span', attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    f_results = results[0]
    ftag = f_results.text.replace(",", "")
    goal = round(float(ftag), 2)
    #gtag = '{0:.2f}'.format(ftag)
    return goal