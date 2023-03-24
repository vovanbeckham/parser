import requests
from bs4 import BeautifulSoup


# response = requests.get('https://www.21vek.by/mobile/', timeout=3)
url_site_category = []
url_list = []

def pars(url):
    s = url.split('/')
    while url:
        response = requests.get(url, timeout=10)
        r = response
        soup = BeautifulSoup(r.text, "lxml")
        product_all = soup.find("div", class_="b-content").find_all("span", class_="g-item-data")
        product_img = soup.find("div", class_="b-content").find_all("img", class_="")
        for el, product in enumerate(product_all):
            product_name = product.get("data-name")
            product_price = product.get("data-price")
            url_img = product_img[el].attrs.get("src")
            with open(f'{s[3]}.txt', 'a') as file:
                file.write(f"{product_name} - {product_price}  - {url_img}\n")
            print(f"{product_name} - {product_price}  - {url_img}")
        try:
            page_next = soup.find("div", class_="b-tools cr-tools_paginator g-box_lseparator").find("a",
                                                                                                    rel="next").get(
                "href")
            url = page_next
        except Exception:
            url = False
            print(f"конец !!!!")
        print(url)
        print(response.status_code)


def url_parse(url):
    for i in range(1):
        response = requests.get(url, timeout=10)
        r = response
        soup = BeautifulSoup(r.text, "lxml")
        url_all = soup.find_all("a", class_="cloud-sub__header")
        for url in url_all:
            name = url.text
            url = url.get("href")
            url_list.append(url)


def url_cat():
    with open("site_21vek.html") as file:
        r = file.read()
    soup = BeautifulSoup(r, "lxml")
    url_21vek = soup.find_all("a", class_="styles_categoryContainer__299CX styles_categoryButton__2mHCm")
    for url in url_21vek:

        url ="https://www.21vek.by"+ url.get("href")
        url_site_category.append(url)
    print(url_site_category)



def main():
    url_cat()
    #pars('https://www.21vek.by/mobile/')



if __name__ == "__main__":
    main()

