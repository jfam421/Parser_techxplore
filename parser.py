import requests as req
from bs4 import BeautifulSoup
import re 

articles = []
URL = "https://phys.org/technology-news/"
HEADERS = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
 
def get_html(url, params=None):
    r = req.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("article", class_ = "sorted-article")
    
    for item in items:
        articles.append({
            item.find("a", class_ = "news-link").get_text() : item.find("a", class_ = "news-link").get("href")})

def parse_site(articles):
    html2 = ""
    text = ""
    for article in articles:
        for key in article:    
            html = get_html(article[key]).text
            soup = BeautifulSoup(html, "html.parser")
            html2 = str(soup.find("div", class_="mt-4 text-low-up text-regular article-main"))
                
            soup2 = BeautifulSoup(html2, "html.parser")
            text = str(soup2.find("p").get_text())

            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

            if regex.search(string) == None:
                with open(str(key) + ".txt", "w", encoding='utf-8') as file:
                    file.write(text)      
            else:
                with open(str(key[0:10]) + ".txt", "w", encoding='utf-8') as file:
                    file.write(text)                
    
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error")

if __name__ == "__main__":
    parse()
    parse_site(articles)
    
