import requests
from bs4 import BeautifulSoup
import pandas

dec_url="https://www.decathlon.in/active-wear-2021/active-wear-for-women-21713?icm=minibanner&icn=ACTIVEWOMENW21&page="
page_num_total = int(input("Enter the number of pages: "))
scraped_product_list = []

for page_num in range(1, page_num_total+1):
    url = dec_url + str(page_num)
    print("\nGet Request for: " + url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_products = soup.find_all("li", {"class":"ais-Hits-item"})

    for product in all_products:
        product_dict = {}
        product_dict["Name"] = product.find("div", {"class":"mb-3 card-title"}).text
        product_dict["Price"] = product.find("button", {"class": "price_tag"}).text
        product_dict["Rating"] = product.find("span", {"class": "rate_number"}).text
        product_dict["MRP"] = product.find("div", {"class": "discount_price"}).text
        try:
            product_dict["Number Of Colours"] = product.find("p", {"class":"mb-0"}).text
        except AttributeError:
            product_dict["Number Of Colours"] = "None"
        scraped_product_list.append(product_dict)

dataFrame = pandas.DataFrame(scraped_product_list)
print("\nCreating CSV File....")

dataFrame.to_csv("Decathlon.csv")
print("\nCSV File Created!")
        
