from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "https://www.snapdeal.com/products/computers-graphic-cards"
uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()

# converting to a soup
page_soup = soup(page_html, "html.parser")

# grabs each container
containers = page_soup.findAll("div", {"class":"product-tuple-description"})

for container in containers:
    productName = container.div.p["title"]
    price = container.div.div.find("span", "product-price")["data-price"]
    print(productName, price)
