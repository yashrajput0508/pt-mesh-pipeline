
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def clean():

    data = pd.read_json('ADB-main\dummy-data-product\sample-output\product.csv')

    for i in data.columns:

        if data[i].type == float or data[i].dtype == int:
            data[i].fillna(data[i].mean(), inplace=True)

        data.fillna('None',inplace=True)

    data.to_json('product.csv')
