import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_cwgc():
    # months = [(01-01,31-01),(01-02,28-02),(01-03,31-03),(01-04,30-04),()]
    url = "https://www.cwgc.org/find/find-war-dead/results?war=1&servedWith=Canadian&tab=wardead&pageSize=100&casualtypagenumber=1"
    print(url)
    col = ['Last_Name','First_Name', 'Rank', 'Service_Number', 'Date_Death', 'Age', 'Cemetary', 'Regiment']
    result = pd.DataFrame(columns = col)

    while(True):
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'lxml')
        table = soup.find(name='table')
        records = table.tbody.findAll('tr')
        df_list = []

        for row in records:
            td_values = row.findAll('td')
            data_row = []
            data_row.append(td_values[4].text)
            data_row.append((td_values[1].find('strong').text.replace('\n','')))
            data_row.extend([td.text for td in td_values[5:11]])
            data_dict = dict(zip(col,data_row))
            df_list.append(result)
            result = result.append(data_dict,ignore_index = True)
        del df_list

        next_page = soup.find('a',attrs= {'class':"paginate_button next"})
        if next_page is None:
            break
        url = "https://www.cwgc.org/find/find-war-dead/results" + next_page.get('href')
        print(url)
        time.sleep(2)

    result.to_csv('records.csv')

def main():
    scrape_cwgc()
    print('Done')

if __name__ == "__main__":
	sys.exit(main())