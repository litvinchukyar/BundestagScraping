import requests
from bs4 import BeautifulSoup
import json
import random
from time import sleep



# people_url_list = []
# for i in range(0, 740, 12):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}"
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     people = soup.find_all('a')
#
#     for person in people:
#         person_page_url = person.get('href')
#         people_url_list.append(person_page_url)
#
# with open('people_url_list.txt', 'a') as file:
#     for line in people_url_list:
#         file.write(f'{line}\n')

with open('people_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    data_dict = []

    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, "lxml")
        person = soup.find(class_="bt-biografie-name").find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_="bt-link-extern")
        social_networks_url = []
        for item in social_networks:
            social_networks_url.append(item.get('href'))

        data = {
            "person_name": person_name,
            "person_company": person_company,
            "social_networks": social_networks_url
        }

        count += 1

        sleep(random.randrange(2, 4))

        print(f'{count}: {line} is done')

        data_dict.append(data)

        with open('data.json', "w") as json_file:
            json.dump(data_dict, json_file, indent=4)







