import requests
from bs4 import BeautifulSoup
import lxml
import csv


# def get_html(url):
#     response = requests.get(url).text
#     return response


# def writer_csv(data: dict):
#     with open('mashina_kg.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], 
#                         data['image'],
#                         data['desc'],
#                         data['price_dollar'],
#                         data['price_som']])


# def get_last_page(html):
#     soup = BeautifulSoup(html, 'lxml')
#     list_of_pages = soup.find('ul',class_="pagination").find_all('a',class_="page-link")
#     int_ = []
#     for i in list_of_pages:
#         num = i.get('data-page')
#         if type(num) == str:
#             int_.append(num)
#     # print(int_)
#     last_page = int_[-1]
#     # print(last_page)
#     return int(last_page)

# """ пробный 

# httt = requests.get('https://www.mashina.kg/search/all/').text
# get_last_page(httt)


# """



# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     car_list = soup.find('div',class_="search-results-table").find_all('div',class_="list-item list-label")
#     # print(car_list)
#     for car in car_list:
#         try:
#             title = car.find('h2',class_="name").text.strip()
#         except AttributeError:
#             title = 'no name'
#         # print(title)

#         try:
#             image = car.find('img').attrs.get('data-src')
#         except AttributeError:
#             image = 'no image'
#         # print(image)

#         try:
#             desc = car.find('div',class_="block info-wrapper item-info-wrapper").text.split()
#             desc = ''.join(desc)
#         except AttributeError:
#             desc = 'no description'
#         # print(desc)

#         try:
#             price_dollar = car.find('div',class_="block price").find('strong').text.strip()
#             price_dollar = ''.join(price_dollar)
#         except AttributeError:
#             price_dollar = 'no price'
#         # print(price_dollar)

#         try:
#             price_som = car.find('div',class_="block price").find('p').text.replace(price_dollar,'').strip()
#             price_som = ''.join(price_som)
#         except AttributeError:
#             price_som = 'no price'
#         # print(price_som)
        
#         cars_dict ={
#                 'title':title,
#                 'image':image,
#                 'desc':desc,
#                 'price_dollar':price_dollar,
#                 'price_som':price_som
#                 }
        
#         writer_csv(cars_dict)


# def main(categories: int):
#     url_of_page = 'https://www.mashina.kg/commercialsearch/all/?type='
#     if categories == 1:
#         parsing_url = url_of_page[:23] + url_of_page[33:-6]
#         html = get_html(parsing_url)
#         get_data(html)
#         number = get_last_page(html)
#         for i in range(2,number+1):
#             url_with_pages = parsing_url + '?page=' + str(i)
#             html = get_html(url_with_pages)
#             get_data(html)
#             print(f'page: {i}')

#     elif categories == 2:
#         parsing_url = url_of_page + str(categories)
#         html = get_html(parsing_url)
#         get_data(html)
#         number = get_last_page(html)
#         for i in range(2,number+1):
#             url_with_pages = parsing_url + '&page=' + str(i)
#             html = get_html(url_with_pages)
#             get_data(html)
#             print(f'page: {i}')

#     elif categories == 3:
#         parsing_url = url_of_page + str(categories)
#         html = get_html(parsing_url)
#         get_data(html)
#         number = get_last_page(html)
#         for i in range(2,number+1):
#             url_with_pages = parsing_url + '&page=' + str(i)
#             html = get_html(url_with_pages)
#             get_data(html)
#             print(f'page: {i}')



# with open('mashina_kg.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['title', 'img', 'description', 'price_dollar', 'price_som'])

# # main(1) -> легковые
# # main(2) -> легкие коммерческие
# # main(3) -> тягачи
# main(1)
