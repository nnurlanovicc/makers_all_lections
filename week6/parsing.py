'''Веб-срейпинг'''

# это технология, получения данных 
# с веб-страниц путем извлечения 

'''парсинг -> анализ даанных, '''
#автоматический сбор данных и структурирование этих данных

# requests -> отправляет запрос на сайт, в итоге получаем html код страницы 

# lxml -> хорошо разбирается в html, выступает в роли парсера (анализирует, 
# разбирает информацию на мелкие части для beautifulsoup4)

# Beautifulsoup4 -> помогает извлекать информацию из HTML. 
# Позваоляет обращяться к определнным тешам и вытаскивать из них данные


# import requests
# import lxml
# from bs4 import BeautifulSoup
# import csv

# def writer_csv(data):
#     with open('data.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([
#                         data['title'], 
#                         data['image'],
#                         data['description'],
#                         data['price'] 
#                         ])


# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     page_list = soup.find('div', class_='page_wrap').find_all('li')
#     last_page = page_list[-1].text
#     return int(last_page)
    



# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     # print(soup)
#     product_list = soup.find('div',class_='list-view').find_all('div',class_='item')
#     # print(product_list)
#     for product in product_list:
#         title = product.find('div',class_='listbox_title').find('strong').text
#         # print(title)
#         image = 'https://www.kivano.kg/' + product.find('img').get('src')
#         # print(image)
#         description = product.find('div',class_='product_text pull-left').text.replace(title,'').strip()
#         # print(description)
#         price = product.find('div',class_='listbox_price').text.strip()
#         # print(price)

#         product_dict = {
#                     'title':title,
#                     'image':image,
#                     'description':description,
#                     'price':price
#                         }
#         writer_csv(product_dict)
        
        


# def main():
#     notebook_url = 'https://www.kivano.kg/noutbuki'
#     html = get_html(notebook_url)
#     get_data(html)
#     number = get_total_pages(html)
#     for i in range(2,number+1):
#         url_with_page = notebook_url + '?page=' + str(i)
#         html = get_html(url_with_page)
#         get_data(html)


# with open('data.csv', 'w') as file:
#     write_ = csv.writer(file)
#     write_.writerow([
#                     'title      ',
#                     'img        ',
#                     'desc       ',
#                     'price      '
#                     ])


# main()






a = 'https://www.mashina.kg/commercialsearch/all/?type='

print(a[:23] + a[33:-6])























"""=================================== task in classroom ==========================================="""


# 1

# def count_lines(file):
#     with open(file,) as f:
#         lines = f.readlines()
#     return len(lines)


# def count_chars_and_words(file):
#     with open(file) as f:
#         lines = f.readlines()
#     line_stat = []
#     for i in lines:
#         line = i.strip()
#         num_chars = len(line)
#         num_words = len(line.split())
#         line_stat.append(num_chars,num_words)
#     return line_stats


# file = 'makers.txt'
# num_line = count_lines(file)
# line_stats = count_chars_and_words(file)

# print(f'количество строк: {num_line}')

# for x,y in enumerate(line_stats):
#     line_num = x + 1
#     num_chars, num_words = y
#     print(f'строка {line_num}: символов - {num_chars}, слов - {num_words}')




# 2
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: True if x > 0 else False,list_))
# print(result)




# 3
 
# from functools import reduce
# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x,y: x + y,list_)
# print(result)



# 4
# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# result = list(zip(list1,list2))
# print(result)




# 2.1
# import requests
# from bs4 import BeautifulSoup
# import csv

# response = requests.get('https://vesti.kg/').text

# soup = BeautifulSoup(response,'lxml')
# li = soup.find('div',class_="nspLinkScroll2").text.strip()
# print(li)


# with open('vesti.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow([li])



# 2.2
# import requests
# from bs4 import BeautifulSoup
# import csv

# response = requests.get('https://www.kinopoisk.ru/lists/movies/top250/').text
# soup = BeautifulSoup(response,'lxml')
# print(soup)






















































"""========================= tasks in plotform ============================"""

# 1
# import requests
# source = requests.get('https://stackoverflow.com/questions').status_code
# print(source)




# 2
# source = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(source, 'lxml')
# print(f'h1:{my_page.h1.text}')
# print(f'p:{my_page.p.text}')
# print(f'a:{my_page.a.get("href")}')


# 3
# sourse = requests.get('https://www.wikipedia.org/').text
# my_page = BeautifulSoup(sourse, 'lxml')
# deutsch = my_page.find('div', class_='central-featured-lang lang5').text
# print(deutsch)



# 4
# def getTitle(url):
#     sourse = requests.get(url).text
#     my_page = BeautifulSoup(sourse, 'lxml')
#     try:
#         h1 = my_page.find('h1')
#     except Exception as e:
#         return "Title could not be found"
#     return h1

# print(getTitle('http://www.example.com/'))



# def getTitle(url):
#     sourse = requests.get(url).text
#     my_page = BeautifulSoup(sourse, 'lxml')
#     h1 = my_page.find('h1')
#     if h1 != None:
#         return h1
#     else:
#         return "Title could not be found"

# print(getTitle('http://www.example.com/'))

"""
sourse = requests.get('http://www.example.com/').text
my_page = BeautifulSoup(sourse, 'lxml')
print(my_page.find('h1').text)
"""



# 5
# import requests 
# from bs4 import BeautifulSoup as BS 
# def find_category(categories: list, keyword: str): 
#     result = [] 
#     for category in categories: 
#         if keyword.lower() in category.lower(): 
#             result.append(category) 
#     return result 
# category_list = [] 
# URL = 'https://enter.kg/' 
# response = requests.get(URL) 
# soup = BS(response.text, 'html.parser') 
# categories = soup.find_all('li', {'class': 'VmClose'}) 
# for category in categories: 
#     title = category.find('a').text 
#     category_list.append(title) 
# categories = soup.find_all("span", {"class": "category-product-count"}) 
# for category in categories: 
#     title = category.text.strip() 
#     category_list.append(title) 
# print(find_category(category_list, 'Ноутбуки'))


# 6
# import requests
# from bs4 import BeautifulSoup
# import lxml

# headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3"}

# response = requests.get('https://www.imdb.com/chart/top', headers=headers).text
# # print(response)
# soup = BeautifulSoup(response, 'lxml')
# li = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base").find_all('li')
# for tit in li:
#     title_list = tit.find('h3',class_="ipc-title__text")
#     print(title_list)






# def get_html(url):
#     response = requests.get(url, headers=headers)
#     print(response)
#     return response.text


# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     title_list = soup.find_all('h3')
#     # print(title_list)

# def main():
#     url = 'https://www.imdb.com/chart/top' 
#     html = get_html(url)
#     get_data(html)



# def get_link(list_: list, name: str):
