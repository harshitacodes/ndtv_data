import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

try:
    page_no = int(input("enter the page no:"))

    news_url = "https://www.ndtv.com/india/page-" + str(page_no)

    page = requests.get(news_url)
    soup = BeautifulSoup(page.text,"html.parser")

    def scrape_the_news(url):

        main_div = soup.find('div', class_ = "ins_wid990")
        sub_div = main_div.find('div',class_ = "ins_lftcont640 clr")
        new_table = sub_div.find('div',class_ = "ins_left_rhs")
        next_table = new_table.find('div',class_ = "ins_lftcont650")
        news_row = next_table.find('div',class_ = "new_storylising")
        news_lines = news_row.find('ul')
        all_data_news = news_lines.find_all('li')

        for news in all_data_news:
                try:
                    news_headline = news.find('h2',class_ = 'nstory_header').get_text().strip()
                    print(news_headline)

                    date_time = news.find('div',class_ = 'nstory_dateline').get_text().strip()
                    # print(date_time)
                    image_icon = news.find('div').img['src']
                    # print(image_icon)
                except Exception as error:
                    pass
            
    scrape_the_news(news_url)

except Exception as e:
    print("page doesn't exists........")