from bs4 import BeautifulSoup


#response = requests.get('https://www.21vek.by/mobile/', timeout=3)
#print(response.status_code)
#r = response


with open("index.html") as file:
    r = file.read()
soup = BeautifulSoup(r, "lxml")
phone_all = soup.find_all("span", class_="g-item-data")
page_next = soup.find("div", class_="b-tools cr-tools_paginator g-box_lseparator").find_all("a")

for phone in phone_all:
    phone_name = phone.get("data-name")
    phone_price = phone.get("data-price")
    print(f"{phone_name}     {phone_price}")

print(page_next)
for page in page_next:
    print(page.text)


