import bs4
import requests
from bs4 import BeautifulSoup

n = 50


while n != 0:
    print("1.Технический писатель")
    print("2.Тестировщик ПО")
    print("3.Специалист по информационной безопасности")
    print("4.Системный программист")
    print("5.Системный аналитик")
    print("6.Системный админимтратор")
    print("7.Разработчик мобильных приложений")
    print("8.Проектировщик 3D-печати в строительстве")
    print("9.Продакт-менеджер")
    print("10.Программист Ruby")
    print("11.Программист Python")
    print("12.Программист PHP")
    print("13.Программист Perl")
    print("14.Программист Java")
    print("15.Программист C++")
    print("16.Программист 1С")
    print("17.Программист")
    print("18.3D-дизайнер")
    print("19.Back-end разработчик")
    print("20.CRM-менеджер")
    print("21.Email маркетолог")
    print("22.ERP-консультант")
    print("23.Front-end разработчик")
    print("24.IT-директор")
    print("25.PR-менеджер")
    print("26.SEO-специалист")
    print("27.SMM-менеджер")
    print("28.UI дизайнер")
    print("29.UX дизайнер")
    print("30.Аналитик Big Data")
    print("31.Веб-аналитик")
    print("32.Веб-дизайнер")
    print("33.Графический дизайнер")
    print("34.Дизайнер машинного обучения")
    print("35.Интернет-маркетолог")
    print("36.Интернет-медиапланер")
    print("37.ИТ-архитектор")
    print("38.Контент-менеджер")
    print("39.Куратор впечатлений")
    print("40.Менеджер по контекстной рекламе")
    print("41.Менеджер по продажам IT-услуг")
    print("42.Менеджер проекта")
    print('43.Администратор баз данных')








    print('0.Выйти\n')


    print("Выберите проффесию\n")


    n = int(input())
    if n == 1:
        url = 'https://buduguru.org/profession/8'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div','skills')
        item2 = page.find('div','typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n",' ')
        d = d.replace("\t\t\t\t\t",' ')
        d = d.replace(".",'.\n')

        print(d)
        print(item1.text)
    if n == 2:
        url = 'https://buduguru.org/profession/10'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 3:
        url = 'https://buduguru.org/profession/17'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 4:
        url = 'https://buduguru.org/profession/38'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 5:
        url = 'https://buduguru.org/profession/15'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)

    if n == 6:
        url = 'https://buduguru.org/profession/16'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 7:
        url = 'https://buduguru.org/profession/35'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 8:
        url = 'https://buduguru.org/profession/44'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 9:
        url = 'https://buduguru.org/profession/5'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 10:
        url = 'https://buduguru.org/profession/29'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 11:
        url = 'https://buduguru.org/profession/32'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 12:
        url = 'https://buduguru.org/profession/28'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 13:
        url = 'https://buduguru.org/profession/33'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 14:
        url = 'https://buduguru.org/profession/27'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 15:
        url = 'https://buduguru.org/profession/31'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 16:
        url = 'https://buduguru.org/profession/30'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 17:
        url = 'https://buduguru.org/profession/9'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 18:
        url = 'https://buduguru.org/profession/18'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 19:
        url = 'https://buduguru.org/profession/45'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 20:
        url = 'https://buduguru.org/profession/26'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 21:
        url = 'https://buduguru.org/profession/1'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 22:
        url = 'https://buduguru.org/profession/14'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 23:
        url = 'https://buduguru.org/profession/46'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 24:
        url = 'https://buduguru.org/profession/24'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 25:
        url = 'https://buduguru.org/profession/42'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 26:
        url = 'https://buduguru.org/profession/20'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 27:
        url = 'https://buduguru.org/profession/7'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 28:
        url = 'https://buduguru.org/profession/36'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 29:
        url = 'https://buduguru.org/profession/19'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 30:
        url = 'https://buduguru.org/profession/39'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 31:
        url = 'https://buduguru.org/profession/23'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 32:
        url = 'https://buduguru.org/profession/12'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 33:
        url = 'https://buduguru.org/profession/37'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 34:
        url = 'https://buduguru.org/profession/48'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 35:
        url = 'https://buduguru.org/profession/25'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 36:
        url = 'https://buduguru.org/profession/40'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 37:
        url = 'https://buduguru.org/profession/2'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 38:
        url = 'https://buduguru.org/profession/6'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 39:
        url = 'https://buduguru.org/profession/47'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 40:
        url = 'https://buduguru.org/profession/3'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 41:
        url = 'https://buduguru.org/profession/41'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 42:
        url = 'https://buduguru.org/profession/11'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)
    if n == 43:
        url = 'https://buduguru.org/profession/4'
        response = requests.get(url)

        page = bs4.BeautifulSoup(response.content, 'html.parser')
        item1 = page.find('div', 'skills')
        item2 = page.find('div', 'typo')

        d = ''.join(item2.text)
        d = d.replace("\n\n\n\n", ' ')
        d = d.replace("\t\t\t\t\t", ' ')
        d = d.replace(".", '.\n')

        print(d)
        print(item1.text)