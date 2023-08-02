import requests
from bs4 import BeautifulSoup
import lxml
import csv
from datetime import datetime






def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = BeautifulSoup(html,'lxml')
    return soup


def get_data(soup):
    news = soup.find_all('div', class_="Tag--article")
    data =[]
    # count = 0
    for i in news[:20]:
        info = i.find('a', class_="ArticleItem--name")
        title = info.text
        img = i.find('img').get('src')
        link = info.get('href')
        description_soup = get_soup(get_html(link))
        description = description_soup.find('div', class_="Article--text").text.replace('\n', '')

        data.append([title,img,description])

        # count += 1
        # if count == 20:
        #     break

    return data




def main():
    curretn_datetime = datetime.now()
    part1 = 'https://kaktus.media/?lable=8&date='
    part2 = str(curretn_datetime.year) + '-' + str(curretn_datetime.month) + '-' + str(curretn_datetime.day) + '&order=time'
    url = part1 + part2 
    html = get_html(url)
    soup = get_soup(html)
    data = get_data(soup)
    return data
    
    


if __name__ == '__main__':
    main()
