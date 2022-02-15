import requests
from bs4 import BeautifulSoup as Bs

city = input("Enter city: ")

url = f'https://ua.sinoptik.ua/погода-{city}'

response = requests.get(url)
html = Bs(response.content, 'html.parser')


def today():
    for i in html.select('#bd1'):
        temp_min = i.select('.temperature > .min >span')[0].text
        temp_max = i.select('.temperature > .max >span')[0].text
        date = i.select('.date ')[0].text
        month = i.select('.month ')[0].text

    description = html.select('#bd1c > .wDescription > .rSide > .description')[0].text
    second_description = html.select('#bd1c > .oDescription > .rSide > .description')[0].text
    print(f'Сьогодні {date} {month}\nmin temperature - {temp_min}\nmax temperature - {temp_max}\n'
          f'{description}\n{second_description}')


today()
# def tomorrow():
#     for i in html.select('#bd2'):
#         temp_min = i.select('.temperature > .min >span')[0].text
#         temp_max = i.select('.temperature > .max >span')[0].text
#         date = i.select('.date ')[0].text
#         month = i.select('.month ')[0].text
#
#     description = html.select('#bd2c > .wDescriptions::before > .rSide > .description::after')[0].text
#     # second_description = html.select('#bd2c > .oDescription > .rSide > .description')[0].text
#     print(f'Сьогодні {date} {month}\nmin temperature - {temp_min}\nmax temperature - {temp_max}\n')
#           # f'{description}\n{second_description}')
