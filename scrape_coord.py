import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_coordinates(cemeteries):
    print(1)


def main():
    data = pd.read_csv('records.csv')
    cemeteries = data.Cemetery.unique()
    print(cemeteries)
    get_coordinates(cemeteries)



if __name__ == "__main__":
	sys.exit(main())