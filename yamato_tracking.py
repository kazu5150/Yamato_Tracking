import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


def YamatoTracking(TrackingCode):
    url = "https://toi.kuronekoyamato.co.jp/cgi-bin/tneko" 
    r = requests.post(url, {"number01":TrackingCode, "number00":1})
    soup = BeautifulSoup(r.text, "html.parser")
    rs = soup.find("div", class_="tracking-invoice-block-detail")   #修正箇所
    rs = [i for i in rs.text.splitlines()]
    rs = [rs[3:][idx:idx + 5] for idx in range(0,len(rs[3:]), 5)]    #修正箇所
    df = pd.DataFrame(rs[1:], columns = rs[0]) 
    
    print(tabulate(df, headers="keys", tablefmt="psql")) 


YamatoTracking(391335074480)