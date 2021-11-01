import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def scrap():
    title = []
    status = []
    posting_date = []
    deadline_date = []

    data = []

    for i in range(0,1235):
        URL = "https://www.adb.org/projects/tenders?page=" + str(i)

        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html.parser')

        for i in soup.find_all('div', attrs={'class': 'item'}):
            title.append(i.find('div', attrs={'class': 'item-title'}).a.text)
            status.append(i.find_all('span')[1].text)
            deadline_date.append(i.find_all('span')[3].text)
            posting_date.append(i.find('div', attrs={'class': 'item-summary'}).text.split(":")[-1].strip(" "))

    data = {'title':title,
            'status':status,
            'posting_date':posting_date,
            'deadline_date':deadline_date}

    dataframe = pd.DataFrame(data)

    dataframe.to_csv(r"product.csv")

scrap()
