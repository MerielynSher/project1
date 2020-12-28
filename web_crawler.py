import bs4
import requests

# 1 simple request
# html = requests.get('http://www.baidu.com')
# print(html.text)

# 2 adding header
# head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
# html = requests.get('https://www.sina.com.cn/', headers=head)
# html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
# print(html.text)

# 3 using beatifulsoup to parse html content
from bs4 import BeautifulSoup
page = requests.get("https://www.monster.com/jobs/search/?q=Software-Developer&where=USA")
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# # Find Elements by ID
results = soup.find(id='ResultsContainer')
print(results.prettify())
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    # print(title_elem)
    # print(company_elem)
    # print(location_elem)
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

# print(list(soup.children))
# [type(item) for item in list(soup.children)]
# html = list(soup.children)[2]
# list(html.children)

# crawling libs


# 5 exercise craw pictures from https://unsplash.com/s/photos/new-year
import urllib.parse
import json
import jsonpath








