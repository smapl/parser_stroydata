from bs4 import BeautifulSoup
import requests
import csv


link_spisok = []
for i in range(51):
    url = f"https://stroydata.ru/msk.html?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find("ul", {"class": "list-firms"})
    link_list = links.find_all("li")
    for li in link_list:
        link = li.find("a").get("href")

        link_spisok.append(link)

data = []
print("pars data")
count = 0
for lk in link_spisok:
    data_in_page = []
    url = f"https://stroydata.ru{lk}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    info = soup.find("dl", {"class": "list-space-plus"})
    full = info.find_all("dd")

    for each in full:
        full[full.index(each)] = each.text
    data.append(full)
    print(f"{count} : {url}")
    count += 1

with open("pars.csv", "a") as fl:
    writer = csv.writer(fl)
    head = [
        "Полное наименование,Адрес,Телефон,E-mail,Сайт,Специализация,Услуги компании,Штат сотрудников,Директор".split()
    ]

    for row in head:
        writer.writerow(head)

    for row in data:
        writer.writerow(row)
