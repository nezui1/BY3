import bs4
import requests
from bs4 import BeautifulSoup

n = 30

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
