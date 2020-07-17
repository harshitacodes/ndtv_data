import requests 
#importing requests to send http requests to get the data
from bs4 import BeautifulSoup 
# from bs4 importing BeautifilSoup , to find the element from tha html data


try:
    def scrape_the_news(url):
        # to get the data, by using requests.get method
        page = requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")

        main_div = soup.find('div', class_ = "ins_wid990")
        sub_div = main_div.find('div',class_ = "ins_lftcont640 clr")
        new_table = sub_div.find('div',class_ = "ins_left_rhs")
        next_table = new_table.find('div',class_ = "ins_lftcont650")
        news_row = next_table.find('div',class_ = "new_storylising")
        news_lines = news_row.find('ul')
        all_data_news = news_lines.find_all('li')


        # In all_data_news the whole data of news headline will come in list format
        for news in all_data_news:
                try:
                    news_headline = news.find('h2',class_ = 'nstory_header').get_text().strip()
                    print(news_headline)
                    
                    date_time = news.find('div',class_ = 'nstory_dateline').get_text().strip()
                    image_icon = news.find('div').img['src']
                except Exception as error:
                    pass

    news_url = "https://www.ndtv.com/india/page-1"
    # the url of ndtv_news of first page
    
    scrape_the_news(news_url)

    def user_choice():
        while True:
            # enter the page no for next page by user input
            user = input("enter the no, for next page :")
            if user == "no":
                print("thank you for reading........")
                break
            else:
                url = "https://www.ndtv.com/india/page-"+user
                # the url of next pages
                scrape_the_news(url)
    user_choice()

except Exception as e:
    print("page doesn't exists........")