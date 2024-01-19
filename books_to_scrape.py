import requests
from bs4 import BeautifulSoup

url="https://books.toscrape.com/"

def get_text_if_not_none(e):
    if e:
        return e.text.strip() #pour enlever les espaces au debut et a la fin
    else:
        return None
response=requests.get(url)
if response.status_code==200:
    html=response.text
    f=open("books.html","w")
    f.write(html)
    f.close()
    soup = BeautifulSoup(html,'html5lib')
    title=soup.find("h1").text
    print(title)

    #description
    description=get_text_if_not_none(soup.find("p",class_="description"))

    #prices
    p_prices=soup.find_all("p",class_='price_color')
    for p_price in p_prices:
        print("PRICE",p_price.text.lstrip('Â£'))
    #titles
    h3_tags = soup.find_all('h3')
    for h3_tag in h3_tags:
        # Find the <a> tag within the <h3> tag
        a_tag = h3_tag.find('a')
        # Check if an <a> tag is found
        if a_tag:
            title = a_tag.get('title', a_tag.text)
            print("TITLE:", title)
        else:
            print("EROOR")    
else:
    print("ERROR",response.status_code)
print('END')