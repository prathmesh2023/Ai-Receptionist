import requests
from bs4 import BeautifulSoup

def get_news():

    url = "https://dbatu.ac.in/"

    r=requests.get(url)

    r_html = r.text

    soup = BeautifulSoup(r_html, features="html.parser")



    news = soup.find_all(class_="category-posts-internal")[0].text


    return(str(news))

print(get_news())