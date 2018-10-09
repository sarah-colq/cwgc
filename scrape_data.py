import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_cwgc():
    url = "https://www.cwgc.org/find/find-war-dead/results?war=1&servedWith=Canadian"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')
    table = soup.find(name='table')
    # result = pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])
    # print(result)

def main():
    scrape_cwgc()
    print('Done')

if __name__ == "__main__":
	sys.exit(main())