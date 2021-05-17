from plyer import notification
# import pyobjus
import requests
from bs4 import BeautifulSoup

def notify(title,message):
    notification.notify(
        title=title,
        message=message,
        # app_icon="/Users/pranavchauhan/Documents/NOTIFY ME JARVIS/covid.ico",
        timeout=20
    )
def request(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
    # notify("IPL","Stay Safe,Stay Healthy")
    ipldata=request("https://www.iplt20.com/points-table/men/2021")
    soup = BeautifulSoup(ipldata, 'html.parser')
    # print(soup)
    Teams=["MI"]
    for tr in soup.find_all("tr")[1:]:
        mydatastr=""
        mydatastr+=tr.get_text()
        Rank=mydatastr.split("\n")[1]
        Team=mydatastr.split("\n")[6]
        Pld=mydatastr.split("\n")[9]
        Won=mydatastr.split("\n")[10]
        Lost=mydatastr.split("\n")[11]
        Net_RR=mydatastr.split("\n")[14]
        Points=mydatastr.split("\n")[17]
        if Team in Teams:
            notify(
                f"MUMBAI INDIANS",
                f"Team |  Rank | Pld | Won | Lost | Net_RR | Points\n{Team}           {Rank}         {Pld}         {Won}        {Lost}      {Net_RR}        {Points}"
            )









