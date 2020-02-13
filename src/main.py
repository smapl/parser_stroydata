from bs4 import BeautifulSoup
import requests
import csv


urls = []
for i in range(51):
    url = f"https://stroydata.ru/msk.html?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find("ul", {"class": "list-firms"})
    link_list = links.find_all("li")
    for li in link_list:
        link = li.find("a").get("href")
        urls.append(link)

data = []
print("pars data")
count = 0
for lk in urls:
    data_in_page = []
    url = f"https://stroydata.ru{lk}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    info = soup.find("dl", {"class": "list-space-plus"})
    full = info.find_all("dd")

    intermediate_list = []
    for each in full:
        full[full.index(each)] = each.text

    intermediate_list.append(full[-1])
    intermediate_list.append(full[2])
    intermediate_list.append(full[3])

    data.append(intermediate_list)
    print(f"{count} : {url}")
    count += 1

with open("StroyData.csv", "a") as fl:
    writer = csv.writer(fl)
    head = ["Директор,Телефон,E-mail".split(",")]

    for row in head:
        writer.writerow(row)

    for row in data:
        writer.writerow(row)
